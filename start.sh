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

# Create wallet if it doesn't exist
if [ ! -f "/root/.bittensor/wallets/bagbot/coldkey" ]; then
    echo "Creating wallet..."
    printf "/root/.bittensor/wallets/\nbagbot\ndefault\n12\n${WALLET_PW}\n${WALLET_PW}\n" | btcli w create --wallet.name bagbot || true
fi

python3 bagbot.py --nocheck
