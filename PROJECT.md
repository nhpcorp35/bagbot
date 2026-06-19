# bagbot — Project Documentation

## What It Does

bagbot is a grid/band trading bot for Bittensor (dTAO) subnets. It watches configured subnets and automatically buys alpha when prices are low and sells when prices are high, within defined price bands. It is designed for **ranging markets** — it does not trend-follow.

> **Note:** dTAO has been trending strongly, which is a poor fit for grid strategy. taotrend-bot was built as the replacement/complement strategy for trending conditions.

---

## Strategy

### Buy Logic
- Each subnet has a `buy_lower` and `buy_upper` price band
- Bot buys alpha when price is within the buy band
- Amount bought scales with position in the band (more at lower prices)
- Will not buy if current alpha holding is at or near `max_alpha`
- Respects `MAX_TAO_PER_BUY` and `MAX_SLIPPAGE_PERCENT_PER_BUY`

### Sell Logic
- Each subnet has a `sell_lower` and `sell_upper` price band
- Bot sells alpha when price rises into the sell band
- Amount sold scales with position in the band (more at higher prices)
- `sell_lower` must be above `buy_upper × 1.50` (enforced sell floor to prevent selling at a loss)
- Respects `MAX_TAO_PER_SELL`
- Trade cooldown prevents rapid repeated trades

### Power Curve
- `BUY_ZONE_POWER` and `SELL_ZONE_POWER` control how aggressively the bot allocates within the band
- 1.0 = linear, >1.0 = more aggressive early, <1.0 = more conservative early

---

## Active Subnet Settings (`bagbot_settings_overrides.py`)

| Subnet | Buy Lower | Buy Upper | Sell Lower | Sell Upper | Max Alpha |
|---|---|---|---|---|---|
| SN9 (iota) | 0.02275 | 0.03337 | 0.04413 | 0.07350 | 30α |
| SN64 (Chutes) | 0.05176 | 0.07591 | 0.08281 | 0.12422 | 30α |
| SN110 (Green Compute) | 0.008 | 0.010 | 0.015 | 0.020 | 30α |

SN9 and SN110 have per-subnet overrides: `max_tao_per_buy: 0.1`, `max_tao_per_sell: 0.1`, `max_slippage: 1.0`.

---

## Important Files

### On Railway Volume (`/data/`)
| File | Purpose |
|---|---|
| `/data/bagbot_state.json` | Bot state: positions, trade log, balances |

### In Repo (`/app/`)
| File | Purpose |
|---|---|
| `bagbot.py` | Main bot logic |
| `bagbot_settings.py` | Default global settings (template) |
| `bagbot_settings_overrides.py` | Active per-subnet settings (overrides defaults on Railway) |
| `taonow_sync.py` | Syncs subnet data from taonow.io API; **GitHub write-back is disabled** to prevent redeploy loops |
| `printHelpers.py` | Logging/display utilities |
| `Procfile` | Railway startup |
| `nixpacks.toml` | Build config |

---

## Environment Variables (Railway)

| Variable | Notes |
|---|---|
| `WALLET_PW` | Bagbot wallet password (loaded via `os.environ` in overrides) |

---

## Wallet

| Field | Value |
|---|---|
| Name | bagbot |
| SS58 Address | `5EASXYiFhQPR6MHzbP3GDrSAcvFKWTVw1iidnzSWbPouAZi2` |
| Validator | Opentensor Foundation `5G3wMP3g3d775hauwmAZioYFVZYnvw6eY46wkFy8hEWD5KP3` |

---

## Key Design Decisions

- **Grid/band strategy** — buy low, sell high within defined price ranges per subnet
- **Sell floor enforcement** — `sell_lower` must be ≥ `buy_upper × 1.50` to prevent selling at a loss
- **Trade cooldown** — prevents rapid repeated trades on volatile price ticks
- **GitHub write-back disabled** — `taonow_sync.py` previously committed `bagbot_settings_overrides.py` hourly, causing Railway rebuild loops. Write-back is now commented out.
- **Pinned subnets** — SN110 is pinned in `taonow_sync.py` so auto-sync never overwrites its settings
- **1 gunicorn worker** — prevents duplicate trade execution

---

## Known Issues / Pending

- Grid strategy is fundamentally mismatched for trending dTAO markets — taotrend-bot is the preferred strategy in trending conditions
- SN9 and SN64 positions were active as of 2026-06-11; monitor for sell triggers
- taonow_sync GitHub write-back is disabled — any settings changes must be committed manually
