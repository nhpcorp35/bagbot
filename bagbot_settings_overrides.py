import os
WALLET_PW = os.environ.get("WALLET_PW", "")
WALLET_NAME = "bagbot"
# Auto-updated by taonow_sync at 2026-05-26 15:43 UTC
SUBNET_SETTINGS = {
    4: {
        'max_alpha': 30,
        'max_tao_per_buy': 0.1,
        'max_tao_per_sell': 0.1,
        'max_slippage_percent_per_buy': 1.0,
        'buy_lower': 0.04335731,
        'buy_upper': 0.06359072,
        'sell_lower': 0.06937169,
        'sell_upper': 0.10405753,
    },
    9: {
        'max_alpha': 30,
        'max_tao_per_buy': 0.1,
        'max_tao_per_sell': 0.1,
        'max_slippage_percent_per_buy': 1.0,
        'buy_lower': 0.02070687,
        'buy_upper': 0.03037008,
        'sell_lower': 0.033131,
        'sell_upper': 0.0496965,
    },
    120: {
        'max_alpha': 30,
        'max_tao_per_buy': 0.1,
        'max_tao_per_sell': 0.1,
        'max_slippage_percent_per_buy': 1.0,
        'buy_lower': 0.04677992,
        'buy_upper': 0.06861056,
        'sell_lower': 0.07484788,
        'sell_upper': 0.11227182,
    },
}
