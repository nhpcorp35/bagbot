import os
WALLET_PW = os.environ.get("WALLET_PW", "")
WALLET_NAME = "bagbot"
# Auto-updated by taonow_sync at 2026-05-26 11:43 UTC
SUBNET_SETTINGS = {
    4: {
        'max_alpha': 30,
        'max_tao_per_buy': 0.1,
        'max_tao_per_sell': 0.1,
        'max_slippage_percent_per_buy': 1.0,
        'buy_lower': 0.04370786,
        'buy_upper': 0.06410487,
        'sell_lower': 0.06993258,
        'sell_upper': 0.10489888,
    },
    9: {
        'max_alpha': 30,
        'max_tao_per_buy': 0.1,
        'max_tao_per_sell': 0.1,
        'max_slippage_percent_per_buy': 1.0,
        'buy_lower': 0.02053577,
        'buy_upper': 0.03011913,
        'sell_lower': 0.03285723,
        'sell_upper': 0.04928585,
    },
    120: {
        'max_alpha': 30,
        'max_tao_per_buy': 0.1,
        'max_tao_per_sell': 0.1,
        'max_slippage_percent_per_buy': 1.0,
        'buy_lower': 0.04731787,
        'buy_upper': 0.06939955,
        'sell_lower': 0.0757086,
        'sell_upper': 0.1135629,
    },
}
