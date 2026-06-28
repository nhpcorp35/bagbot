## 2026-06-28

### bagbot

**staking.log persistence fix**
- Changed log file path from `staking.log` (ephemeral `/app/`) to `/root/.bittensor/staking.log` (persistent volume mount) so trade history survives redeploys

---

# Bagbot Changelog

## 2026-06-11

### Bug fixes
- **Disabled GitHub write-back in `taonow_sync.py`** — `_write_settings_to_github()` was being called every hour, committing `bagbot_settings_overrides.py` and triggering a Railway rebuild each time. Commented out the call. Bot continues to update settings in memory and on the Railway volume as before.

### Configuration
- **Pinned SN110 (Green Compute)** — Added SN110 to `PINNED_SUBNETS` in `taonow_sync.py` so taonow_sync never auto-overwrites its settings.
- **Added SN110 to `bagbot_settings_overrides.py`** — buy_upper: τ0.010, sell_lower: τ0.015, sell_upper: τ0.020, max_alpha: 30.

### Notes
- Bagbot wallet `5EASXYiFhQPR6MHzbP3GDrSAcvFKWTVw1iidnzSWbPouAZi2` topped up with ~τ0.5. Free balance τ0.2233 — below MAX_TAO_PER_BUY (τ0.3) so no buys firing yet.
- Active positions: SN9 (iota, 13.5α), SN64 (Chutes, 4.4α). SN110 at τ0.0109, just above buy_upper.
- 17 failed Railway deployments overnight traced to AWS US West incident + hourly taonow_sync commits (now fixed).
