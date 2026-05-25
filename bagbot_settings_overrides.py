import os
WALLET_PW = os.environ.get("WALLET_PW", "")
WALLET_NAME = "bagbot"
# Auto-updated by taonow_sync at 2026-05-25 18:48 UTC
SUBNET_SETTINGS = {
    4: {
        'max_alpha': 30,
        'max_tao_per_buy': 0.1,
        'max_tao_per_sell': 0.1,
        'max_slippage_percent_per_buy': 1.0,
        'buy_lower': 0.04347164,
        'buy_upper': 0.06375841,
        'sell_lower': 0.06955463,
        'sell_upper': 0.10433195,
    },
    9: {
        'max_alpha': 30,
        'max_tao_per_buy': 0.1,
        'max_tao_per_sell': 0.1,
        'max_slippage_percent_per_buy': 1.0,
        'buy_lower': 0.02055945,
        'buy_upper': 0.03015386,
        'sell_lower': 0.03289512,
        'sell_upper': 0.04934268,
    },
    120: {
        'max_alpha': 30,
        'max_tao_per_buy': 0.1,
        'max_tao_per_sell': 0.1,
        'max_slippage_percent_per_buy': 1.0,
        'buy_lower': 0.04695766,
        'buy_upper': 0.06887124,
        'sell_lower': 0.07513226,
        'sell_upper': 0.1126984,
    },
}
