import os
WALLET_PW = os.environ.get("WALLET_PW", "")
WALLET_NAME = "bagbot"
# Auto-updated by taonow_sync at 2026-06-10 12:41 UTC
SUBNET_SETTINGS = {
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
    64: {
        'buy_lower': 0.05176,
        'buy_upper': 0.07591,
        'max_alpha': 30,
        'sell_lower': 0.08281,
        'sell_upper': 0.12422,
    },
    110: {
        'max_alpha': 30,
        'max_tao_per_buy': 0.1,
        'max_tao_per_sell': 0.1,
        'max_slippage_percent_per_buy': 1.0,
        'buy_lower': 0.00680917,
        'buy_upper': 0.00998678,
        'sell_lower': 0.01089467,
        'sell_upper': 0.016342,
    },
}
