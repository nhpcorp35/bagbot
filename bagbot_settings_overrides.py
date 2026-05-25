import os
WALLET_PW = os.environ.get("WALLET_PW", "")
WALLET_NAME = "bagbot"
# Auto-updated by taonow_sync at 2026-05-25 17:53 UTC
SUBNET_SETTINGS = {
    4: {
        'max_alpha': 30,
        'max_tao_per_buy': 0.1,
        'max_tao_per_sell': 0.1,
        'max_slippage_percent_per_buy': 1.0,
        'buy_lower': 0.03477732,
        'buy_upper': 0.05912144,
        'sell_lower': 0.08114707,
        'sell_upper': 0.14490548,
    },
    9: {
        'max_alpha': 30,
        'max_tao_per_buy': 0.1,
        'max_tao_per_sell': 0.1,
        'max_slippage_percent_per_buy': 1.0,
        'buy_lower': 0.01644756,
        'buy_upper': 0.02796085,
        'sell_lower': 0.03837764,
        'sell_upper': 0.0685315,
    },
    62: {
        'buy_lower': 0.00850827,
        'buy_upper': 0.0,
        'sell_lower': 0.01616571,
        'sell_upper': 0.02552481,
        'max_alpha': 1,
        'max_tao_per_buy': 0.0,
        'max_tao_per_sell': 0.1,
        'max_slippage_percent_per_buy': 1.0,
    },
    120: {
        'max_alpha': 30,
        'max_tao_per_buy': 0.1,
        'max_tao_per_sell': 0.1,
        'max_slippage_percent_per_buy': 1.0,
        'buy_lower': 0.03756613,
        'buy_upper': 0.06386242,
        'sell_lower': 0.08765431,
        'sell_upper': 0.15652555,
    },
}
