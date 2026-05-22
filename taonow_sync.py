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
"""

import asyncio
import logging
import os
import time
import urllib.request
import urllib.error
import json
import base64

logger = logging.getLogger(__name__)

TAONOW_URL          = "https://taonow.io/api/cache"
SCORE_THRESHOLD     = 80.0
MAX_SUBNETS         = 3
POLL_INTERVAL_HOURS = 1

GITHUB_TOKEN        = os.environ.get("GITHUB_TOKEN", "")
BAGBOT_GITHUB_REPO  = "nhpcorp35/bagbot"
BAGBOT_SETTINGS_PATH = "bagbot_settings_overrides.py"
GITHUB_API          = "https://api.github.com"

# Default per-subnet config applied to any taonow-selected subnet.
DEFAULT_SUBNET_CONFIG = {
    "max_alpha":                    30,
    "max_tao_per_buy":              0.10,
    "max_tao_per_sell":             0.10,
    "max_slippage_percent_per_buy": 1.0,
}


def _fetch_taonow():
    """Fetch /api/cache from taonow. Returns parsed JSON or None on failure."""
    try:
        req = urllib.request.Request(
            TAONOW_URL,
            headers={"User-Agent": "bagbot/1.0"},
        )
        with urllib.request.urlopen(req, timeout=10) as resp:
            return json.loads(resp.read().decode())
    except Exception as e:
        logger.warning(f"taonow_sync: fetch failed ({e}) — keeping existing settings")
        return None


def _build_settings_from_positions(positions):
    """
    Pick top MAX_SUBNETS subnets scoring >= SCORE_THRESHOLD and build
    SUBNET_SETTINGS entries using live prices from the API response.
    Returns a dict or None if no qualifying subnets found.
    """
    qualifying = [
        p for p in positions
        if p.get("score") is not None
        and p.get("score") >= SCORE_THRESHOLD
        and p.get("netuid") not in (None, 0)
        and p.get("price") is not None
        and p.get("price") > 0
    ]

    if not qualifying:
        return None

    qualifying.sort(key=lambda p: p["score"], reverse=True)
    top = qualifying[:MAX_SUBNETS]

    new_settings = {}
    for p in top:
        netuid = int(p["netuid"])
        price  = float(p["price"])
        cfg = dict(DEFAULT_SUBNET_CONFIG)
        cfg["buy_lower"]  = round(price * 0.60, 8)
        cfg["buy_upper"]  = round(price * 1.02, 8)
        cfg["sell_lower"] = round(price * 1.40, 8)
        cfg["sell_upper"] = round(price * 2.50, 8)
        new_settings[netuid] = cfg
        logger.info(
            f"taonow_sync: SN{netuid} selected (score={p['score']:.1f}, "
            f"price=τ{price:.6f}, buy<τ{cfg['buy_upper']:.6f}, sell>τ{cfg['sell_lower']:.6f})"
        )

    return new_settings


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
        logger.warning("taonow_sync: GITHUB_TOKEN not set — skipping GitHub write-back")
        return

    try:
        headers = {
            "Authorization": f"Bearer {GITHUB_TOKEN}",
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
            "Content-Type": "application/json",
        }

        # Get current file SHA
        url = f"{GITHUB_API}/repos/{BAGBOT_GITHUB_REPO}/contents/{BAGBOT_SETTINGS_PATH}"
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as resp:
            file_data = json.loads(resp.read().decode())
        sha = file_data["sha"]

        # Build new content
        new_content = _build_settings_py(new_settings)
        encoded = base64.b64encode(new_content.encode()).decode()

        # Commit
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


def sync_settings(bagbot_settings):
    """
    Fetch taonow scores, update SUBNET_SETTINGS in memory, and write back to GitHub.
    Safe to call at any time — never raises, never clears settings on failure.
    """
    logger.info("taonow_sync: fetching scores from taonow.io...")
    data = _fetch_taonow()
    if data is None:
        return

    positions = data.get("positions", [])
    if not positions:
        logger.warning("taonow_sync: no positions in response — keeping existing settings")
        return

    new_settings = _build_settings_from_positions(positions)
    if not new_settings:
        logger.warning(
            f"taonow_sync: no subnets scored >= {SCORE_THRESHOLD} — keeping existing settings"
        )
        return

    old_subnets = set(bagbot_settings.SUBNET_SETTINGS.keys())
    new_subnets = set(new_settings.keys())

    if old_subnets != new_subnets:
        added   = new_subnets - old_subnets
        removed = old_subnets - new_subnets
        if added:   logger.info(f"taonow_sync: adding subnets {added}")
        if removed: logger.info(f"taonow_sync: removing subnets {removed}")

    bagbot_settings.SUBNET_SETTINGS = new_settings
    logger.info(f"taonow_sync: SUBNET_SETTINGS updated → {list(new_subnets)}")

    # Write back to GitHub so taonow settings panel stays in sync
    _write_settings_to_github(new_settings)


async def polling_loop(bagbot_settings):
    """
    Async background loop — syncs once immediately at startup then every
    POLL_INTERVAL_HOURS hours. Never crashes the bot on failure.
    """
    while True:
        try:
            sync_settings(bagbot_settings)
        except Exception as e:
            logger.error(f"taonow_sync: unexpected error in polling_loop: {e}")
        await asyncio.sleep(POLL_INTERVAL_HOURS * 3600)
