import os
WALLET_PW = os.environ.get("WALLET_PW", "")
WALLET_NAME = "bagbot"
# Auto-updated by taonow_sync at 2026-05-27 06:18 UTC
SUBNET_SETTINGS = {
    4: {
        'buy_lower': 0.02866488,
        'buy_upper': 0.0,
        'sell_lower': 0.05446328,
        'sell_upper': 0.08599465,
        'max_alpha': 1,
        'max_tao_per_buy': 0.0,
        'max_tao_per_sell': 0.1,
        'max_slippage_percent_per_buy': 1.0,
    },
    9: {
        'buy_lower': 0.01466694,
        'buy_upper': 0.0,
        'sell_lower': 0.02786718,
        'sell_upper': 0.04400081,
        'max_alpha': 1,
        'max_tao_per_buy': 0.0,
        'max_tao_per_sell': 0.1,
        'max_slippage_percent_per_buy': 1.0,
    },
    120: {
        'buy_lower': 0.03124233,
        'buy_upper': 0.0,
        'sell_lower': 0.05936043,
        'sell_upper': 0.09372699,
        'max_alpha': 1,
        'max_tao_per_buy': 0.0,
        'max_tao_per_sell': 0.1,
        'max_slippage_percent_per_buy': 1.0,
    },
}
