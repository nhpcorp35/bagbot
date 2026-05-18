#!/bin/bash
set -e

# Fix scalecodec conflict
pip uninstall scalecodec cyscale -y
pip install cyscale --force-reinstall

# Write settings overrides
printf "WALLET_PW = '%s'\nWALLET_NAME = 'bagbot'\nMAX_TAO_PER_BUY = 0.02\nMAX_TAO_PER_SELL = 0.02\nMAX_SLIPPAGE_PERCENT_PER_BUY = 0.2\nSUBNET_SETTINGS = {19: {'buy_lower': 0.010500, 'buy_upper': 0.012500, 'sell_lower': 0.014500, 'sell_upper': 0.018000, 'max_alpha': 20}, 11: {'buy_lower': 0.007500, 'buy_upper': 0.009400, 'sell_lower': 0.011000, 'sell_upper': 0.014000, 'max_alpha': 25}}\n" "$WALLET_PW" > /app/bagbot_settings_overrides.py

# Clear old wallet and copy fresh one
rm -rf /root/.bittensor/wallets/bagbot
mkdir -p /root/.bittensor/wallets
cp -r /app/wallet_backup /root/.bittensor/wallets/bagbot

python3 bagbot.py --nocheck
