import os
WALLET_PW = os.environ.get("WALLET_PW", "")
WALLET_NAME = "bagbot"
# Auto-updated by taonow_sync at 2026-05-26 23:35 UTC
SUBNET_SETTINGS = {
    4: {
        'max_alpha': 30,
        'max_tao_per_buy': 0.1,
        'max_tao_per_sell': 0.1,
        'max_slippage_percent_per_buy': 1.0,
        'buy_lower': 0.04332884,
        'buy_upper': 0.06354897,
        'sell_lower': 0.06932614,
        'sell_upper': 0.10398922,
    },
    9: {
        'max_alpha': 30,
        'max_tao_per_buy': 0.1,
        'max_tao_per_sell': 0.1,
        'max_slippage_percent_per_buy': 1.0,
        'buy_lower': 0.0209112,
        'buy_upper': 0.03066975,
        'sell_lower': 0.03345791,
        'sell_upper': 0.05018687,
    },
    120: {
        'max_alpha': 30,
        'max_tao_per_buy': 0.1,
        'max_tao_per_sell': 0.1,
        'max_slippage_percent_per_buy': 1.0,
        'buy_lower': 0.04684935,
        'buy_upper': 0.06871238,
        'sell_lower': 0.07495896,
        'sell_upper': 0.11243844,
    },
}
