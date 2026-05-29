import os
WALLET_PW = os.environ.get("WALLET_PW", "")
WALLET_NAME = "bagbot"
# Auto-updated by taonow_sync at 2026-05-29 08:54 UTC
SUBNET_SETTINGS = {
    4: {
        'max_alpha': 30,
        'max_tao_per_buy': 0.1,
        'max_tao_per_sell': 0.1,
        'max_slippage_percent_per_buy': 1.0,
        'buy_lower': 0.04206389,
        'buy_upper': 0.0616937,
        'sell_lower': 0.06730222,
        'sell_upper': 0.10095333,
    },
    9: {
        'buy_lower': 0.02274917,
        'buy_upper': 0.03336545,
        'max_alpha': 30,
        'max_slippage_percent_per_buy': 1,
        'max_tao_per_buy': 0.1,
        'max_tao_per_sell': 0.1,
        'sell_lower': 0.04413,
        'sell_upper': 0.0735,
    },
    62: {
        'max_alpha': 30,
        'max_tao_per_buy': 0.1,
        'max_tao_per_sell': 0.1,
        'max_slippage_percent_per_buy': 1.0,
        'buy_lower': 0.01300455,
        'buy_upper': 0.01907334,
        'sell_lower': 0.02080728,
        'sell_upper': 0.03121092,
    },
    64: {
        'buy_lower': 0.05176,
        'buy_upper': 0.07591,
        'max_alpha': 30,
        'sell_lower': 0.08281,
        'sell_upper': 0.12422,
    },
    120: {
        'max_alpha': 30,
        'max_tao_per_buy': 0.1,
        'max_tao_per_sell': 0.1,
        'max_slippage_percent_per_buy': 1.0,
        'buy_lower': 0.04736782,
        'buy_upper': 0.0694728,
        'sell_lower': 0.07578851,
        'sell_upper': 0.11368276,
    },
}
