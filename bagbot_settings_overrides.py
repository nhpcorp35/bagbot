import os
WALLET_PW = os.environ.get("WALLET_PW", "")
WALLET_NAME = "bagbot"
# Auto-updated by taonow_sync at 2026-05-24 04:23 UTC
SUBNET_SETTINGS = {
    4: {
        'max_alpha': 30,
        'max_tao_per_buy': 0.1,
        'max_tao_per_sell': 0.1,
        'max_slippage_percent_per_buy': 1.0,
        'buy_lower': 0.0335739,
        'buy_upper': 0.05707562,
        'sell_lower': 0.07833909,
        'sell_upper': 0.13989124,
    },
    9: {
        'max_alpha': 30,
        'max_tao_per_buy': 0.1,
        'max_tao_per_sell': 0.1,
        'max_slippage_percent_per_buy': 1.0,
        'buy_lower': 0.01575999,
        'buy_upper': 0.02679199,
        'sell_lower': 0.03677331,
        'sell_upper': 0.06566663,
    },
    100: {
        'buy_lower': 0.00649103,
        'buy_upper': 0.0,
        'sell_lower': 0.01233296,
        'sell_upper': 0.01947309,
        'max_alpha': 1,
        'max_tao_per_buy': 0.0,
        'max_tao_per_sell': 0.1,
        'max_slippage_percent_per_buy': 1.0,
    },
    120: {
        'max_alpha': 30,
        'max_tao_per_buy': 0.1,
        'max_tao_per_sell': 0.1,
        'max_slippage_percent_per_buy': 1.0,
        'buy_lower': 0.03862784,
        'buy_upper': 0.06566733,
        'sell_lower': 0.09013162,
        'sell_upper': 0.16094933,
    },
}
