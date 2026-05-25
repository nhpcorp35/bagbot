import os
WALLET_PW = os.environ.get("WALLET_PW", "")
WALLET_NAME = "bagbot"
# Auto-updated by taonow_sync at 2026-05-25 05:39 UTC
SUBNET_SETTINGS = {
    4: {
        'buy_lower': 0.02869009,
        'buy_upper': 0.0,
        'sell_lower': 0.05451117,
        'sell_upper': 0.08607026,
        'max_alpha': 1,
        'max_tao_per_buy': 0.0,
        'max_tao_per_sell': 0.1,
        'max_slippage_percent_per_buy': 1.0,
    },
    9: {
        'buy_lower': 0.01384816,
        'buy_upper': 0.0,
        'sell_lower': 0.0263115,
        'sell_upper': 0.04154448,
        'max_alpha': 1,
        'max_tao_per_buy': 0.0,
        'max_tao_per_sell': 0.1,
        'max_slippage_percent_per_buy': 1.0,
    },
    62: {
        'buy_lower': 0.00882066,
        'buy_upper': 0.0,
        'sell_lower': 0.01675926,
        'sell_upper': 0.02646199,
        'max_alpha': 1,
        'max_tao_per_buy': 0.0,
        'max_tao_per_sell': 0.1,
        'max_slippage_percent_per_buy': 1.0,
    },
}
