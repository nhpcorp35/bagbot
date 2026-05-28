import os
WALLET_PW = os.environ.get("WALLET_PW", "")
WALLET_NAME = "bagbot"
# Auto-updated by taonow_sync at 2026-05-28 20:28 UTC
SUBNET_SETTINGS = {
    4: {
        'buy_lower': 0.02810487,
        'buy_upper': 0.0,
        'sell_lower': 0.05339924,
        'sell_upper': 0.0843146,
        'max_alpha': 1,
        'max_tao_per_buy': 0.0,
        'max_tao_per_sell': 0.1,
        'max_slippage_percent_per_buy': 1.0,
    },
    9: {
        'buy_lower': 0.02274917,
        'buy_upper': 0.03336545,
        'max_alpha': 30,
        'max_slippage_percent_per_buy': 1,
        'max_tao_per_buy': 0.1,
        'max_tao_per_sell': 0.1,
        'sell_lower': 0.03639868,
        'sell_upper': 0.05459801,
    },
    64: {
        'buy_lower': 0.05176,
        'buy_upper': 0.07591,
        'max_alpha': 30,
        'sell_lower': 0.08281,
        'sell_upper': 0.12422,
    },
    120: {
        'buy_lower': 0.03119528,
        'buy_upper': 0.0,
        'sell_lower': 0.05927104,
        'sell_upper': 0.09358585,
        'max_alpha': 1,
        'max_tao_per_buy': 0.0,
        'max_tao_per_sell': 0.1,
        'max_slippage_percent_per_buy': 1.0,
    },
}
