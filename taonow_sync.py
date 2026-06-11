"""
taonow_sync.py — polls taonow.io for top-scoring subnets and updates
SUBNET_SETTINGS in memory. Falls back gracefully if taonow is unreachable.
Also writes selected settings back to GitHub so the taonow bot settings panel
stays in sync with what the bot is actually trading.

Rules:
- Only subnets scoring >= SCORE_THRESHOLD qualify
- Max MAX_SUBNETS subnets traded at once
- If taonow is unreachable, keep existing settings untouched
- Polls every POLL_INTERVAL_HOURS hours
- Subnets with existing holdings that fall below threshold get sell-only settings
"""

import asyncio
import logging
import os
import time
import urllib.request
import json
import base64

logger = logging.getLogger(__name__)

TAONOW_URL           = "https://taonow.io/api/cache"
SCORE_THRESHOLD      = 65.0
MAX_SUBNETS          = 3
POLL_INTERVAL_HOURS  = 1

GITHUB_TOKEN         = os.environ.get("GITHUB_TOKEN", "")
BAGBOT_GITHUB_REPO   = "nhpcorp35/bagbot"
BAGBOT_SETTINGS_PATH = "bagbot_settings_overrides.py"
GITHUB_API           = "https://api.github.com"

DEFAULT_SUBNET_CONFIG = {
    "max_alpha":                    30,
    "max_tao_per_buy":              0.10,
    "max_tao_per_sell":             0.10,
    "max_slippage_percent_per_buy": 1.0,
}


TAONOW_PASSWORD = os.environ.get("PASSWORD", "")

# Subnets in this list are never touched by taonow_sync — thresholds you set
# manually in the bot settings panel will be preserved across every sync.
# Add/remove subnet IDs here to pin/unpin them.
PINNED_SUBNETS = {9, 64}  # SN9 iota, SN64 Chutes — manually managed

def _fetch_taonow():
    """Fetch /api/cache from taonow. Returns parsed JSON or None on failure."""
    try:
        headers = {"User-Agent": "bagbot/1.0"}
        if TAONOW_PASSWORD:
            credentials = base64.b64encode(f"user:{TAONOW_PASSWORD}".encode()).decode()
            headers["Authorization"] = f"Basic {credentials}"
        req = urllib.request.Request(TAONOW_URL, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as resp:
            return json.loads(resp.read().decode())
    except Exception as e:
        logger.warning(f"taonow_sync: fetch failed ({e}) — keeping existing settings")
        return None


def _build_settings_from_positions(positions, current_holdings, data=None):
    """
    Pick top MAX_SUBNETS subnets scoring >= SCORE_THRESHOLD and build
    SUBNET_SETTINGS entries using live prices from the API response.
    Also adds sell-only settings for any held subnets not in the top selection.
    Returns a dict or None if no qualifying subnets found.
    """
    # Build price lookup from pool data (more complete than positions)
    pool = (data or {}).get("pool", {})
    price_lookup = {
        int(k): float(v["price"])
        for k, v in pool.items()
        if v.get("price")
    }
    # Fall back to positions prices if pool missing any
    for p in positions:
        netuid = p.get("netuid")
        if netuid and int(netuid) not in price_lookup and p.get("price"):
            price_lookup[int(netuid)] = float(p["price"])

    logger.info(f"taonow_sync: got {len(positions)} positions, {len([p for p in positions if p.get('score') is not None])} with scores")
    qualifying = [
        p for p in positions
        if p.get("score") is not None
        and p.get("score") >= SCORE_THRESHOLD
        and p.get("netuid") not in (None, 0)
        and int(p["netuid"]) not in PINNED_SUBNETS  # pinned subnets are never auto-managed
        and price_lookup.get(int(p["netuid"]))  # price must be in pool data
    ]

    if not qualifying:
        # Even if nothing qualifies, still add sell-only for held positions
        new_settings = {}
    else:
        qualifying.sort(key=lambda p: p["score"], reverse=True)
        top = qualifying[:MAX_SUBNETS]
        new_settings = {}
        for p in top:
            netuid = int(p["netuid"])
            price  = price_lookup.get(netuid)
            if not price:
                logger.warning(f"taonow_sync: SN{netuid} has no price in pool — skipping")
                continue
            cfg = dict(DEFAULT_SUBNET_CONFIG)
            cfg["buy_lower"]  = round(price * 0.75, 8)  # Buy aggressively down to 25% below current
            cfg["buy_upper"]  = round(price * 1.10, 8)  # Buy up to 10% below current (was 2%)
            cfg["sell_lower"] = round(price * 1.20, 8)  # Start selling at 20% above current (was 40%)
            cfg["sell_upper"] = round(price * 1.80, 8)  # Sell hard at 80% above (was 150%)
            new_settings[netuid] = cfg
            logger.info(
                f"taonow_sync: SN{netuid} selected (score={p['score']:.1f}, "
                f"price=τ{price:.6f}, buy<τ{cfg['buy_upper']:.6f}, sell>τ{cfg['sell_lower']:.6f})"
            )

    # Add sell-only settings for held subnets not in the new selection
    active_netuids = set(new_settings.keys())  # subnets already added as active
    for netuid, alpha in current_holdings.items():
        if netuid in active_netuids:
            continue  # Already being actively traded — don't override
        if netuid == 0:
            continue  # Skip root subnet
        if netuid in PINNED_SUBNETS:
            continue  # Pinned — never auto-manage
        if alpha < 0.001:
            continue  # Dust, not worth selling
        price = price_lookup.get(netuid)
        if not price:
            logger.warning(f"taonow_sync: SN{netuid} has {alpha:.4f} alpha but no price data — skipping sell-only")
            continue
        # Sell immediately — set sell_lower just below current price
        cfg = {
            "buy_lower":  round(price * 0.50, 8),  # Never reached since buy_upper=0
            "buy_upper":  0.0,                      # Never buy more
            "sell_lower": round(price * 0.95, 8),  # Start selling now (5% below current)
            "sell_upper": round(price * 1.50, 8),  # Sell hard at 50% above
            "max_alpha":  1,            # Must be >= 1 to pass validation; effectively 0 since buy_upper=0
            "max_tao_per_buy":  0.0,
            "max_tao_per_sell": 0.10,
            "max_slippage_percent_per_buy": 1.0,
        }
        new_settings[netuid] = cfg
        logger.info(
            f"taonow_sync: SN{netuid} added as sell-only "
            f"({alpha:.4f} alpha held, price=τ{price:.6f}, sell>τ{cfg['sell_lower']:.6f})"
        )

    return new_settings if new_settings else None


def _build_settings_py(subnet_settings):
    """Build the full bagbot_settings_overrides.py content."""
    lines = [
        "import os",
        'WALLET_PW = os.environ.get("WALLET_PW", "")',
        'WALLET_NAME = "bagbot"',
        f"# Auto-updated by taonow_sync at {time.strftime('%Y-%m-%d %H:%M UTC', time.gmtime())}",
        "SUBNET_SETTINGS = {",
    ]
    for netuid, cfg in sorted(subnet_settings.items()):
        lines.append(f"    {netuid}: {{")
        for k, v in cfg.items():
            lines.append(f"        {repr(k)}: {repr(v)},")
        lines.append("    },")
    lines.append("}")
    return "\n".join(lines) + "\n"


def _write_settings_to_github(new_settings):
    """
    Commit updated SUBNET_SETTINGS to bagbot GitHub repo.
    Fails silently — bot keeps trading even if GitHub write fails.
    """
    if not GITHUB_TOKEN:
        # Try loading dynamically in case env var was set after module load
        token = os.environ.get("GITHUB_TOKEN", "")
        if not token:
            logger.warning("taonow_sync: GITHUB_TOKEN not set — skipping GitHub write-back")
            return
    else:
        token = GITHUB_TOKEN

    try:
        headers = {
            "Authorization": f"Bearer {token}",
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
            "Content-Type": "application/json",
        }

        url = f"{GITHUB_API}/repos/{BAGBOT_GITHUB_REPO}/contents/{BAGBOT_SETTINGS_PATH}"
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as resp:
            file_data = json.loads(resp.read().decode())
        sha = file_data["sha"]

        new_content = _build_settings_py(new_settings)
        encoded = base64.b64encode(new_content.encode()).decode()

        payload = json.dumps({
            "message": f"taonow_sync: auto-update to SN{sorted(new_settings.keys())}",
            "content": encoded,
            "sha": sha,
        }).encode()

        req = urllib.request.Request(url, data=payload, headers=headers, method="PUT")
        with urllib.request.urlopen(req, timeout=15) as resp:
            result = json.loads(resp.read().decode())
            commit_sha = result.get("commit", {}).get("sha", "")[:7]
            logger.info(f"taonow_sync: settings written to GitHub (commit {commit_sha})")

    except Exception as e:
        logger.error(f"taonow_sync: GitHub write-back failed ({e}) — bot continues trading")


def sync_settings(bagbot_settings, current_holdings=None):
    """
    Fetch taonow scores, update SUBNET_SETTINGS in memory, and write back to GitHub.
    current_holdings: dict of {netuid: alpha_amount} for sell-only logic.
    Safe to call at any time — never raises, never clears settings on failure.
    """
    logger.info("taonow_sync: fetching scores from taonow.io...")
    data = _fetch_taonow()
    if data is None:
        return

    positions = data.get("positions", [])
    logger.info(f"taonow_sync: got {len(positions)} positions from taonow")
    if not positions:
        logger.warning("taonow_sync: no positions in response — keeping existing settings")
        return

    holdings = current_holdings or {}
    logger.info(f"taonow_sync: current holdings = {holdings}")
    new_settings = _build_settings_from_positions(positions, holdings, data)
    if not new_settings:
        logger.warning(
            f"taonow_sync: no subnets scored >= {SCORE_THRESHOLD} and no held positions — keeping existing settings"
        )
        return

    old_subnets = set(bagbot_settings.SUBNET_SETTINGS.keys())
    new_subnets = set(new_settings.keys())

    if old_subnets != new_subnets:
        added   = new_subnets - old_subnets
        removed = old_subnets - new_subnets
        if added:   logger.info(f"taonow_sync: adding subnets {added}")
        if removed: logger.info(f"taonow_sync: removing subnets {removed}")

    # Preserve pinned subnet settings from current config
    for netuid in PINNED_SUBNETS:
        if netuid in bagbot_settings.SUBNET_SETTINGS:
            new_settings[netuid] = bagbot_settings.SUBNET_SETTINGS[netuid]
            logger.info(f"taonow_sync: SN{netuid} is pinned — preserving existing settings")

    bagbot_settings.SUBNET_SETTINGS = new_settings
    logger.info(f"taonow_sync: SUBNET_SETTINGS updated → {list(new_settings.keys())}")

    # _write_settings_to_github(new_settings)  # disabled: git commits trigger unnecessary Railway rebuilds


async def polling_loop(bagbot_settings, get_holdings_fn=None):
    """
    Async background loop — waits for first stats refresh, then syncs
    immediately and every POLL_INTERVAL_HOURS hours after that.
    get_holdings_fn: optional callable that returns {netuid: alpha} dict.
    """
    # Wait for first stats refresh to complete before syncing
    await asyncio.sleep(60)
    while True:
        try:
            holdings = get_holdings_fn() if get_holdings_fn else {}
            sync_settings(bagbot_settings, holdings)
        except Exception as e:
            logger.error(f"taonow_sync: unexpected error in polling_loop: {e}")
        await asyncio.sleep(POLL_INTERVAL_HOURS * 3600)

