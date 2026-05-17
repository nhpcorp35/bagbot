#!/bin/bash
pip uninstall scalecodec cyscale -y
pip install cyscale --force-reinstall
mkdir -p /root/.bittensor/wallets
cp -r /app/wallet_backup /root/.bittensor/wallets/bagbot
python3 bagbot.py --nocheck
