import os
WALLET_PW = os.environ.get("WALLET_PW", "")
WALLET_NAME = "bagbot"
# Auto-updated by taonow_sync at 2026-05-26 08:59 UTC
SUBNET_SETTINGS = {
    4: {
        'buy_lower': 0.02913858,
        'buy_upper': 0.0,
        'sell_lower': 0.0553633,
        'sell_upper': 0.08741573,
        'max_alpha': 1,
        'max_tao_per_buy': 0.0,
        'max_tao_per_sell': 0.1,
        'max_slippage_percent_per_buy': 1.0,
    },
    9: {
        'buy_lower': 0.01369051,
        'buy_upper': 0.0,
        'sell_lower': 0.02601198,
        'sell_upper': 0.04107154,
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
