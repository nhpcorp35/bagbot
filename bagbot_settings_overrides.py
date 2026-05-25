import os
WALLET_PW = os.environ.get("WALLET_PW", "")
WALLET_NAME = "bagbot"
# Auto-updated by taonow_sync at 2026-05-25 20:45 UTC
SUBNET_SETTINGS = {
    4: {
        'buy_lower': 0.0289811,
        'buy_upper': 0.0,
        'sell_lower': 0.05506408,
        'sell_upper': 0.08694329,
        'max_alpha': 1,
        'max_tao_per_buy': 0.0,
        'max_tao_per_sell': 0.1,
        'max_slippage_percent_per_buy': 1.0,
    },
    9: {
        'buy_lower': 0.0137063,
        'buy_upper': 0.0,
        'sell_lower': 0.02604197,
        'sell_upper': 0.0411189,
        'max_alpha': 1,
        'max_tao_per_buy': 0.0,
        'max_tao_per_sell': 0.1,
        'max_slippage_percent_per_buy': 1.0,
    },
    120: {
        'buy_lower': 0.03130511,
        'buy_upper': 0.0,
        'sell_lower': 0.05947971,
        'sell_upper': 0.09391533,
        'max_alpha': 1,
        'max_tao_per_buy': 0.0,
        'max_tao_per_sell': 0.1,
        'max_slippage_percent_per_buy': 1.0,
    },
}
