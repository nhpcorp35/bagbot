#!/bin/bash
set -e

# Fix scalecodec conflict
pip uninstall scalecodec cyscale -y
pip install cyscale --force-reinstall

# Inject wallet password from environment variable into settings overrides
sed "s/WALLET_PW = os.environ.get(\"WALLET_PW\", \"\")/WALLET_PW = '$WALLET_PW'/" /app/bagbot_settings_overrides.py > /tmp/bagbot_settings_overrides_final.py
cp /tmp/bagbot_settings_overrides_final.py /app/bagbot_settings_overrides.py

# Clear old wallet and copy fresh one
rm -rf /root/.bittensor/wallets/bagbot
mkdir -p /root/.bittensor/wallets
cp -r /app/wallet_backup /root/.bittensor/wallets/bagbot

python3 bagbot.py --nocheck
