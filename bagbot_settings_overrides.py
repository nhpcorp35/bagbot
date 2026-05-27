import os
WALLET_PW = os.environ.get("WALLET_PW", "")
WALLET_NAME = "bagbot"
# Auto-updated by taonow_sync at 2026-05-27 00:17 UTC
SUBNET_SETTINGS = {
    4: {
        'buy_lower': 0.02862879,
        'buy_upper': 0.0,
        'sell_lower': 0.05439471,
        'sell_upper': 0.08588638,
        'max_alpha': 1,
        'max_tao_per_buy': 0.0,
        'max_tao_per_sell': 0.1,
        'max_slippage_percent_per_buy': 1.0,
    },
    9: {
        'buy_lower': 0.01467698,
        'buy_upper': 0.0,
        'sell_lower': 0.02788626,
        'sell_upper': 0.04403093,
        'max_alpha': 1,
        'max_tao_per_buy': 0.0,
        'max_tao_per_sell': 0.1,
        'max_slippage_percent_per_buy': 1.0,
    },
    120: {
        'buy_lower': 0.03127361,
        'buy_upper': 0.0,
        'sell_lower': 0.05941985,
        'sell_upper': 0.09382082,
        'max_alpha': 1,
        'max_tao_per_buy': 0.0,
        'max_tao_per_sell': 0.1,
        'max_slippage_percent_per_buy': 1.0,
    },
}
