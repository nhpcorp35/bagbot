import os
WALLET_PW = os.environ.get("WALLET_PW", "")
WALLET_NAME = "bagbot"
# Auto-updated by taonow_sync at 2026-05-24 23:38 UTC
SUBNET_SETTINGS = {
    4: {
        'buy_lower': 0.0284387,
        'buy_upper': 0.0,
        'sell_lower': 0.05403353,
        'sell_upper': 0.0853161,
        'max_alpha': 1,
        'max_tao_per_buy': 0.0,
        'max_tao_per_sell': 0.1,
        'max_slippage_percent_per_buy': 1.0,
    },
    9: {
        'buy_lower': 0.01367916,
        'buy_upper': 0.0,
        'sell_lower': 0.02599039,
        'sell_upper': 0.04103747,
        'max_alpha': 1,
        'max_tao_per_buy': 0.0,
        'max_tao_per_sell': 0.1,
        'max_slippage_percent_per_buy': 1.0,
    },
    62: {
        'buy_lower': 0.008765,
        'buy_upper': 0.0,
        'sell_lower': 0.0166535,
        'sell_upper': 0.02629499,
        'max_alpha': 1,
        'max_tao_per_buy': 0.0,
        'max_tao_per_sell': 0.1,
        'max_slippage_percent_per_buy': 1.0,
    },
}
