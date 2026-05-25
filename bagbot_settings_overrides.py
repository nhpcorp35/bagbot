import os
WALLET_PW = os.environ.get("WALLET_PW", "")
WALLET_NAME = "bagbot"
# Auto-updated by taonow_sync at 2026-05-25 02:39 UTC
SUBNET_SETTINGS = {
    4: {
        'buy_lower': 0.02864083,
        'buy_upper': 0.0,
        'sell_lower': 0.05441757,
        'sell_upper': 0.08592249,
        'max_alpha': 1,
        'max_tao_per_buy': 0.0,
        'max_tao_per_sell': 0.1,
        'max_slippage_percent_per_buy': 1.0,
    },
    9: {
        'buy_lower': 0.01391448,
        'buy_upper': 0.0,
        'sell_lower': 0.02643752,
        'sell_upper': 0.04174345,
        'max_alpha': 1,
        'max_tao_per_buy': 0.0,
        'max_tao_per_sell': 0.1,
        'max_slippage_percent_per_buy': 1.0,
    },
    62: {
        'buy_lower': 0.00882045,
        'buy_upper': 0.0,
        'sell_lower': 0.01675885,
        'sell_upper': 0.02646135,
        'max_alpha': 1,
        'max_tao_per_buy': 0.0,
        'max_tao_per_sell': 0.1,
        'max_slippage_percent_per_buy': 1.0,
    },
}
