import os
WALLET_PW = os.environ.get("WALLET_PW", "")
WALLET_NAME = "bagbot"
# Auto-updated by taonow_sync at 2026-05-26 05:57 UTC
SUBNET_SETTINGS = {
    4: {
        'buy_lower': 0.02913321,
        'buy_upper': 0.0,
        'sell_lower': 0.0553531,
        'sell_upper': 0.08739964,
        'max_alpha': 1,
        'max_tao_per_buy': 0.0,
        'max_tao_per_sell': 0.1,
        'max_slippage_percent_per_buy': 1.0,
    },
    9: {
        'buy_lower': 0.01371737,
        'buy_upper': 0.0,
        'sell_lower': 0.02606301,
        'sell_upper': 0.04115211,
        'max_alpha': 1,
        'max_tao_per_buy': 0.0,
        'max_tao_per_sell': 0.1,
        'max_slippage_percent_per_buy': 1.0,
    },
    120: {
        'buy_lower': 0.03175679,
        'buy_upper': 0.0,
        'sell_lower': 0.06033791,
        'sell_upper': 0.09527038,
        'max_alpha': 1,
        'max_tao_per_buy': 0.0,
        'max_tao_per_sell': 0.1,
        'max_slippage_percent_per_buy': 1.0,
    },
}
