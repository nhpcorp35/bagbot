import os
WALLET_PW = os.environ.get("WALLET_PW", "")
WALLET_NAME = "bagbot"
# Auto-updated by taonow_sync at 2026-05-26 22:51 UTC
SUBNET_SETTINGS = {
    4: {
        'max_alpha': 30,
        'max_tao_per_buy': 0.1,
        'max_tao_per_sell': 0.1,
        'max_slippage_percent_per_buy': 1.0,
        'buy_lower': 0.04332644,
        'buy_upper': 0.06354545,
        'sell_lower': 0.06932231,
        'sell_upper': 0.10398347,
    },
    9: {
        'max_alpha': 30,
        'max_tao_per_buy': 0.1,
        'max_tao_per_sell': 0.1,
        'max_slippage_percent_per_buy': 1.0,
        'buy_lower': 0.02091227,
        'buy_upper': 0.03067133,
        'sell_lower': 0.03345964,
        'sell_upper': 0.05018945,
    },
    120: {
        'max_alpha': 30,
        'max_tao_per_buy': 0.1,
        'max_tao_per_sell': 0.1,
        'max_slippage_percent_per_buy': 1.0,
        'buy_lower': 0.04685064,
        'buy_upper': 0.06871428,
        'sell_lower': 0.07496103,
        'sell_upper': 0.11244154,
    },
}
