#!/bin/bash
set -e

# Fix scalecodec conflict
pip uninstall scalecodec cyscale -y
pip install cyscale --force-reinstall

# Write settings overrides from env vars
cat > /app/bagbot_settings_overrides.py << SETTINGS
WALLET_PW = "${WALLET_PW}"
WALLET_NAME = "bagbot"
SUBNET_SETTINGS = {}
SETTINGS

# Copy wallet files to bittensor directory
mkdir -p /root/.bittensor/wallets
cp -r /app/wallet_backup /root/.bittensor/wallets/bagbot

python3 bagbot.py --nocheck
