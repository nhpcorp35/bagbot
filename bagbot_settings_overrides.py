import os
WALLET_PW = os.environ.get("WALLET_PW", "")
WALLET_NAME = "bagbot"
# Auto-updated by taonow_sync at 2026-05-26 12:00 UTC
SUBNET_SETTINGS = {
    4: {
        'buy_lower': 0.02885123,
        'buy_upper': 0.0,
        'sell_lower': 0.05481734,
        'sell_upper': 0.08655369,
        'max_alpha': 1,
        'max_tao_per_buy': 0.0,
        'max_tao_per_sell': 0.1,
        'max_slippage_percent_per_buy': 1.0,
    },
    9: {
        'buy_lower': 0.01376795,
        'buy_upper': 0.0,
        'sell_lower': 0.02615911,
        'sell_upper': 0.04130385,
        'max_alpha': 1,
        'max_tao_per_buy': 0.0,
        'max_tao_per_sell': 0.1,
        'max_slippage_percent_per_buy': 1.0,
    },
    120: {
        'buy_lower': 0.03154525,
        'buy_upper': 0.0,
        'sell_lower': 0.05993597,
        'sell_upper': 0.09463575,
        'max_alpha': 1,
        'max_tao_per_buy': 0.0,
        'max_tao_per_sell': 0.1,
        'max_slippage_percent_per_buy': 1.0,
    },
}
