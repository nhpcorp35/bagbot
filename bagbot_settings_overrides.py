import os
WALLET_PW = os.environ.get("WALLET_PW", "")
WALLET_NAME = "bagbot"
# Auto-updated by taonow_sync at 2026-05-26 15:03 UTC
SUBNET_SETTINGS = {
    4: {
        'buy_lower': 0.02890488,
        'buy_upper': 0.0,
        'sell_lower': 0.05491928,
        'sell_upper': 0.08671465,
        'max_alpha': 1,
        'max_tao_per_buy': 0.0,
        'max_tao_per_sell': 0.1,
        'max_slippage_percent_per_buy': 1.0,
    },
    9: {
        'buy_lower': 0.01380463,
        'buy_upper': 0.0,
        'sell_lower': 0.02622879,
        'sell_upper': 0.04141388,
        'max_alpha': 1,
        'max_tao_per_buy': 0.0,
        'max_tao_per_sell': 0.1,
        'max_slippage_percent_per_buy': 1.0,
    },
    120: {
        'buy_lower': 0.03150058,
        'buy_upper': 0.0,
        'sell_lower': 0.0598511,
        'sell_upper': 0.09450174,
        'max_alpha': 1,
        'max_tao_per_buy': 0.0,
        'max_tao_per_sell': 0.1,
        'max_slippage_percent_per_buy': 1.0,
    },
}
