import os
WALLET_PW = os.environ.get("WALLET_PW", "")
WALLET_NAME = "bagbot"
# Auto-updated by taonow_sync at 2026-05-27 10:49 UTC
SUBNET_SETTINGS = {
    4: {
        'max_alpha': 30,
        'max_tao_per_buy': 0.1,
        'max_tao_per_sell': 0.1,
        'max_slippage_percent_per_buy': 1.0,
        'buy_lower': 0.04274807,
        'buy_upper': 0.06269716,
        'sell_lower': 0.0683969,
        'sell_upper': 0.10259536,
    },
    9: {
        'max_alpha': 30,
        'max_tao_per_buy': 0.1,
        'max_tao_per_sell': 0.1,
        'max_slippage_percent_per_buy': 1.0,
        'buy_lower': 0.02208792,
        'buy_upper': 0.03239562,
        'sell_lower': 0.03534068,
        'sell_upper': 0.05301102,
    },
    120: {
        'max_alpha': 30,
        'max_tao_per_buy': 0.1,
        'max_tao_per_sell': 0.1,
        'max_slippage_percent_per_buy': 1.0,
        'buy_lower': 0.0467847,
        'buy_upper': 0.06861756,
        'sell_lower': 0.07485552,
        'sell_upper': 0.11228328,
    },
}
