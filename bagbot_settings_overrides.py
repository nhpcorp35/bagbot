import os
WALLET_PW = os.environ.get("WALLET_PW", "")
WALLET_NAME = "bagbot"
# Auto-updated by taonow_sync at 2026-05-26 00:08 UTC
SUBNET_SETTINGS = {
    4: {
        'max_alpha': 30,
        'max_tao_per_buy': 0.1,
        'max_tao_per_sell': 0.1,
        'max_slippage_percent_per_buy': 1.0,
        'buy_lower': 0.04365907,
        'buy_upper': 0.06403331,
        'sell_lower': 0.06985452,
        'sell_upper': 0.10478177,
    },
    9: {
        'max_alpha': 30,
        'max_tao_per_buy': 0.1,
        'max_tao_per_sell': 0.1,
        'max_slippage_percent_per_buy': 1.0,
        'buy_lower': 0.02080158,
        'buy_upper': 0.03050898,
        'sell_lower': 0.03328252,
        'sell_upper': 0.04992378,
    },
    120: {
        'max_alpha': 30,
        'max_tao_per_buy': 0.1,
        'max_tao_per_sell': 0.1,
        'max_slippage_percent_per_buy': 1.0,
        'buy_lower': 0.04733867,
        'buy_upper': 0.06943005,
        'sell_lower': 0.07574187,
        'sell_upper': 0.11361281,
    },
}
