import os
WALLET_PW = os.environ.get("WALLET_PW", "")
WALLET_NAME = "bagbot"
# Auto-updated by taonow_sync at 2026-05-27 12:19 UTC
SUBNET_SETTINGS = {
    4: {
        'buy_lower': 0.02848104,
        'buy_upper': 0.0,
        'sell_lower': 0.05411398,
        'sell_upper': 0.08544313,
        'max_alpha': 1,
        'max_tao_per_buy': 0.0,
        'max_tao_per_sell': 0.1,
        'max_slippage_percent_per_buy': 1.0,
    },
    9: {
        'buy_lower': 0.01515763,
        'buy_upper': 0.0,
        'sell_lower': 0.0287995,
        'sell_upper': 0.0454729,
        'max_alpha': 1,
        'max_tao_per_buy': 0.0,
        'max_tao_per_sell': 0.1,
        'max_slippage_percent_per_buy': 1.0,
    },
    120: {
        'buy_lower': 0.03131987,
        'buy_upper': 0.0,
        'sell_lower': 0.05950775,
        'sell_upper': 0.09395961,
        'max_alpha': 1,
        'max_tao_per_buy': 0.0,
        'max_tao_per_sell': 0.1,
        'max_slippage_percent_per_buy': 1.0,
    },
}
