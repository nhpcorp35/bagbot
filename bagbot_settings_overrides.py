import os
WALLET_PW = os.environ.get("WALLET_PW", "")
WALLET_NAME = "bagbot"
# Auto-updated by taonow_sync at 2026-05-26 12:44 UTC
SUBNET_SETTINGS = {
    4: {
        'max_alpha': 30,
        'max_tao_per_buy': 0.1,
        'max_tao_per_sell': 0.1,
        'max_slippage_percent_per_buy': 1.0,
        'buy_lower': 0.04327685,
        'buy_upper': 0.06347271,
        'sell_lower': 0.06924296,
        'sell_upper': 0.10386443,
    },
    9: {
        'max_alpha': 30,
        'max_tao_per_buy': 0.1,
        'max_tao_per_sell': 0.1,
        'max_slippage_percent_per_buy': 1.0,
        'buy_lower': 0.02065193,
        'buy_upper': 0.03028949,
        'sell_lower': 0.03304308,
        'sell_upper': 0.04956462,
    },
    120: {
        'max_alpha': 30,
        'max_tao_per_buy': 0.1,
        'max_tao_per_sell': 0.1,
        'max_slippage_percent_per_buy': 1.0,
        'buy_lower': 0.04725087,
        'buy_upper': 0.06930127,
        'sell_lower': 0.07560139,
        'sell_upper': 0.11340209,
    },
}
