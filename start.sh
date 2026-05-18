#!/bin/bash
set -e

# Fix scalecodec conflict
pip uninstall scalecodec cyscale -y
pip install cyscale --force-reinstall

# Write settings overrides
printf "WALLET_PW = '%s'\nWALLET_NAME = 'bagbot'\nSUBNET_SETTINGS = {}\n" "$WALLET_PW" > /app/bagbot_settings_overrides.py

# Debug - show what was written (mask middle chars)
echo "=== Settings file contents ==="
cat /app/bagbot_settings_overrides.py
echo "=============================="

# Clear old wallet and copy fresh one
rm -rf /root/.bittensor/wallets/bagbot
mkdir -p /root/.bittensor/wallets
cp -r /app/wallet_backup /root/.bittensor/wallets/bagbot

python3 bagbot.py --nocheck
