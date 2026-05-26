import os
WALLET_PW = os.environ.get("WALLET_PW", "")
WALLET_NAME = "bagbot"
# Auto-updated by taonow_sync at 2026-05-26 20:36 UTC
SUBNET_SETTINGS = {
    4: {
        'max_alpha': 30,
        'max_tao_per_buy': 0.1,
        'max_tao_per_sell': 0.1,
        'max_slippage_percent_per_buy': 1.0,
        'buy_lower': 0.0433617,
        'buy_upper': 0.06359715,
        'sell_lower': 0.06937871,
        'sell_upper': 0.10406807,
    },
    9: {
        'max_alpha': 30,
        'max_tao_per_buy': 0.1,
        'max_tao_per_sell': 0.1,
        'max_slippage_percent_per_buy': 1.0,
        'buy_lower': 0.02074018,
        'buy_upper': 0.03041893,
        'sell_lower': 0.03318429,
        'sell_upper': 0.04977643,
    },
    120: {
        'max_alpha': 30,
        'max_tao_per_buy': 0.1,
        'max_tao_per_sell': 0.1,
        'max_slippage_percent_per_buy': 1.0,
        'buy_lower': 0.04678092,
        'buy_upper': 0.06861201,
        'sell_lower': 0.07484947,
        'sell_upper': 0.11227421,
    },
}
