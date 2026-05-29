import os
WALLET_PW = os.environ.get("WALLET_PW", "")
WALLET_NAME = "bagbot"
# Auto-updated by taonow_sync at 2026-05-29 04:13 UTC
SUBNET_SETTINGS = {
    4: {
        'max_alpha': 30,
        'max_tao_per_buy': 0.1,
        'max_tao_per_sell': 0.1,
        'max_slippage_percent_per_buy': 1.0,
        'buy_lower': 0.04212328,
        'buy_upper': 0.06178081,
        'sell_lower': 0.06739724,
        'sell_upper': 0.10109586,
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
        'buy_lower': 0.01288812,
        'buy_upper': 0.01890258,
        'sell_lower': 0.020621,
        'sell_upper': 0.0309315,
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
        'buy_lower': 0.0472297,
        'buy_upper': 0.06927023,
        'sell_lower': 0.07556752,
        'sell_upper': 0.11335128,
    },
}
