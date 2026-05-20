"""
taonow_sync.py — polls taonow.io for top-scoring subnets and updates
SUBNET_SETTINGS in memory. Falls back gracefully if taonow is unreachable.

Rules:
- Only subnets scoring >= SCORE_THRESHOLD qualify
- Max MAX_SUBNETS subnets traded at once
- If taonow is unreachable, keep existing settings untouched
- Polls every POLL_INTERVAL_HOURS hours
"""

import asyncio
import logging
import time
import urllib.request
import json

logger = logging.getLogger(__name__)

TAONOW_URL        = "https://taonow.io/api/cache"
SCORE_THRESHOLD   = 80.0
MAX_SUBNETS       = 3
POLL_INTERVAL_HOURS = 1

# Default per-subnet config applied to any taonow-selected subnet.
# buy_upper/sell_lower are set dynamically from live price.
DEFAULT_SUBNET_CONFIG = {
    "max_alpha":                    30,
    "max_tao_per_buy":              0.10,
    "max_tao_per_sell":             0.10,
    "max_slippage_percent_per_buy": 1.0,
    # buy_lower  = 40% below current price (set dynamically)
    # buy_upper  = current price            (set dynamically)
    # sell_lower = 40% above current price  (set dynamically)
    # sell_upper = 2.5x current price       (set dynamically)
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

    # Sort by score descending, take top MAX_SUBNETS
    qualifying.sort(key=lambda p: p["score"], reverse=True)
    top = qualifying[:MAX_SUBNETS]

    new_settings = {}
    for p in top:
        netuid = int(p["netuid"])
        price  = float(p["price"])
        cfg = dict(DEFAULT_SUBNET_CONFIG)
        cfg["buy_lower"]  = round(price * 0.60, 8)   # 40% below current
        cfg["buy_upper"]  = round(price * 1.02, 8)   # slightly above current (catch dips)
        cfg["sell_lower"] = round(price * 1.40, 8)   # 40% above entry
        cfg["sell_upper"] = round(price * 2.50, 8)   # 2.5x entry
        new_settings[netuid] = cfg
        logger.info(
            f"taonow_sync: SN{netuid} selected (score={p['score']:.1f}, "
            f"price=τ{price:.6f}, buy<τ{cfg['buy_upper']:.6f}, sell>τ{cfg['sell_lower']:.6f})"
        )

    return new_settings


def sync_settings(bagbot_settings):
    """
    Fetch taonow scores and update bagbot_settings.SUBNET_SETTINGS in memory.
    Safe to call at any time — never raises, never clears settings on failure.
    """
    logger.info("taonow_sync: fetching scores from taonow.io...")
    data = _fetch_taonow()
    if data is None:
        return  # Already logged warning in _fetch_taonow

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
