import os
WALLET_PW = os.environ.get("WALLET_PW", "")
WALLET_NAME = "bagbot"
# Auto-updated by taonow_sync at 2026-05-26 19:35 UTC
SUBNET_SETTINGS = {
    4: {
        'max_alpha': 30,
        'max_tao_per_buy': 0.1,
        'max_tao_per_sell': 0.1,
        'max_slippage_percent_per_buy': 1.0,
        'buy_lower': 0.04336167,
        'buy_upper': 0.06359712,
        'sell_lower': 0.06937867,
        'sell_upper': 0.10406801,
    },
    9: {
        'max_alpha': 30,
        'max_tao_per_buy': 0.1,
        'max_tao_per_sell': 0.1,
        'max_slippage_percent_per_buy': 1.0,
        'buy_lower': 0.02074009,
        'buy_upper': 0.0304188,
        'sell_lower': 0.03318415,
        'sell_upper': 0.04977622,
    },
    120: {
        'max_alpha': 30,
        'max_tao_per_buy': 0.1,
        'max_tao_per_sell': 0.1,
        'max_slippage_percent_per_buy': 1.0,
        'buy_lower': 0.04678104,
        'buy_upper': 0.06861219,
        'sell_lower': 0.07484967,
        'sell_upper': 0.1122745,
    },
}
