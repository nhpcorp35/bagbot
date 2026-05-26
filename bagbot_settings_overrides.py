import os
WALLET_PW = os.environ.get("WALLET_PW", "")
WALLET_NAME = "bagbot"
# Auto-updated by taonow_sync at 2026-05-26 03:26 UTC
SUBNET_SETTINGS = {
    4: {
        'max_alpha': 30,
        'max_tao_per_buy': 0.1,
        'max_tao_per_sell': 0.1,
        'max_slippage_percent_per_buy': 1.0,
        'buy_lower': 0.04369982,
        'buy_upper': 0.06409307,
        'sell_lower': 0.06991971,
        'sell_upper': 0.10487956,
    },
    9: {
        'max_alpha': 30,
        'max_tao_per_buy': 0.1,
        'max_tao_per_sell': 0.1,
        'max_slippage_percent_per_buy': 1.0,
        'buy_lower': 0.02057606,
        'buy_upper': 0.03017822,
        'sell_lower': 0.03292169,
        'sell_upper': 0.04938254,
    },
    120: {
        'max_alpha': 30,
        'max_tao_per_buy': 0.1,
        'max_tao_per_sell': 0.1,
        'max_slippage_percent_per_buy': 1.0,
        'buy_lower': 0.04763519,
        'buy_upper': 0.06986495,
        'sell_lower': 0.0762163,
        'sell_upper': 0.11432446,
    },
}
