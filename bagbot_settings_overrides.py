import os
WALLET_PW = os.environ.get("WALLET_PW", "")
WALLET_NAME = "bagbot"
# Auto-updated by taonow_sync at 2026-05-25 05:41 UTC
SUBNET_SETTINGS = {
    4: {
        'max_alpha': 30,
        'max_tao_per_buy': 0.1,
        'max_tao_per_sell': 0.1,
        'max_slippage_percent_per_buy': 1.0,
        'buy_lower': 0.03442811,
        'buy_upper': 0.05852778,
        'sell_lower': 0.08033224,
        'sell_upper': 0.14345044,
    },
    9: {
        'max_alpha': 30,
        'max_tao_per_buy': 0.1,
        'max_tao_per_sell': 0.1,
        'max_slippage_percent_per_buy': 1.0,
        'buy_lower': 0.01661779,
        'buy_upper': 0.02825025,
        'sell_lower': 0.03877485,
        'sell_upper': 0.0692408,
    },
    62: {
        'max_alpha': 30,
        'max_tao_per_buy': 0.1,
        'max_tao_per_sell': 0.1,
        'max_slippage_percent_per_buy': 1.0,
        'buy_lower': 0.01060285,
        'buy_upper': 0.01802484,
        'sell_lower': 0.02473998,
        'sell_upper': 0.04417853,
    },
}
