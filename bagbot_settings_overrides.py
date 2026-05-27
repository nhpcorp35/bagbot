import os
WALLET_PW = os.environ.get("WALLET_PW", "")
WALLET_NAME = "bagbot"
# Auto-updated by taonow_sync at 2026-05-27 01:28 UTC
SUBNET_SETTINGS = {
    4: {
        'max_alpha': 30,
        'max_tao_per_buy': 0.1,
        'max_tao_per_sell': 0.1,
        'max_slippage_percent_per_buy': 1.0,
        'buy_lower': 0.04294961,
        'buy_upper': 0.06299276,
        'sell_lower': 0.06871938,
        'sell_upper': 0.10307906,
    },
    9: {
        'max_alpha': 30,
        'max_tao_per_buy': 0.1,
        'max_tao_per_sell': 0.1,
        'max_slippage_percent_per_buy': 1.0,
        'buy_lower': 0.02201532,
        'buy_upper': 0.03228913,
        'sell_lower': 0.03522451,
        'sell_upper': 0.05283676,
    },
    120: {
        'max_alpha': 30,
        'max_tao_per_buy': 0.1,
        'max_tao_per_sell': 0.1,
        'max_slippage_percent_per_buy': 1.0,
        'buy_lower': 0.04691041,
        'buy_upper': 0.06880194,
        'sell_lower': 0.07505666,
        'sell_upper': 0.11258499,
    },
}
