import os
WALLET_PW = os.environ.get("WALLET_PW", "")
WALLET_NAME = "bagbot"
# Auto-updated by taonow_sync at 2026-05-25 04:42 UTC
SUBNET_SETTINGS = {
    4: {
        'max_alpha': 30,
        'max_tao_per_buy': 0.1,
        'max_tao_per_sell': 0.1,
        'max_slippage_percent_per_buy': 1.0,
        'buy_lower': 0.03436899,
        'buy_upper': 0.05842729,
        'sell_lower': 0.08019432,
        'sell_upper': 0.14320414,
    },
    9: {
        'max_alpha': 30,
        'max_tao_per_buy': 0.1,
        'max_tao_per_sell': 0.1,
        'max_slippage_percent_per_buy': 1.0,
        'buy_lower': 0.01669738,
        'buy_upper': 0.02838555,
        'sell_lower': 0.03896056,
        'sell_upper': 0.06957242,
    },
    62: {
        'max_alpha': 30,
        'max_tao_per_buy': 0.1,
        'max_tao_per_sell': 0.1,
        'max_slippage_percent_per_buy': 1.0,
        'buy_lower': 0.0105848,
        'buy_upper': 0.01799416,
        'sell_lower': 0.02469786,
        'sell_upper': 0.04410332,
    },
}
