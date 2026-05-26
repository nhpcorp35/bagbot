import os
WALLET_PW = os.environ.get("WALLET_PW", "")
WALLET_NAME = "bagbot"
# Auto-updated by taonow_sync at 2026-05-26 13:35 UTC
SUBNET_SETTINGS = {
    4: {
        'max_alpha': 30,
        'max_tao_per_buy': 0.1,
        'max_tao_per_sell': 0.1,
        'max_slippage_percent_per_buy': 1.0,
        'buy_lower': 0.04334579,
        'buy_upper': 0.06357382,
        'sell_lower': 0.06935326,
        'sell_upper': 0.10402989,
    },
    9: {
        'max_alpha': 30,
        'max_tao_per_buy': 0.1,
        'max_tao_per_sell': 0.1,
        'max_slippage_percent_per_buy': 1.0,
        'buy_lower': 0.02086723,
        'buy_upper': 0.03060528,
        'sell_lower': 0.03338757,
        'sell_upper': 0.05008136,
    },
    120: {
        'max_alpha': 30,
        'max_tao_per_buy': 0.1,
        'max_tao_per_sell': 0.1,
        'max_slippage_percent_per_buy': 1.0,
        'buy_lower': 0.04724737,
        'buy_upper': 0.06929615,
        'sell_lower': 0.0755958,
        'sell_upper': 0.11339369,
    },
}
