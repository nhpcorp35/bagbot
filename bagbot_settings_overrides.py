import os
WALLET_PW = os.environ.get("WALLET_PW", "")
WALLET_NAME = "bagbot"
# Auto-updated by taonow_sync at 2026-05-24 22:37 UTC
SUBNET_SETTINGS = {
    4: {
        'max_alpha': 30,
        'max_tao_per_buy': 0.1,
        'max_tao_per_sell': 0.1,
        'max_slippage_percent_per_buy': 1.0,
        'buy_lower': 0.03398826,
        'buy_upper': 0.05778004,
        'sell_lower': 0.07930594,
        'sell_upper': 0.14161775,
    },
    9: {
        'max_alpha': 30,
        'max_tao_per_buy': 0.1,
        'max_tao_per_sell': 0.1,
        'max_slippage_percent_per_buy': 1.0,
        'buy_lower': 0.01624739,
        'buy_upper': 0.02762056,
        'sell_lower': 0.03791057,
        'sell_upper': 0.06769746,
    },
    62: {
        'max_alpha': 30,
        'max_tao_per_buy': 0.1,
        'max_tao_per_sell': 0.1,
        'max_slippage_percent_per_buy': 1.0,
        'buy_lower': 0.010518,
        'buy_upper': 0.0178806,
        'sell_lower': 0.02454199,
        'sell_upper': 0.04382499,
    },
}
