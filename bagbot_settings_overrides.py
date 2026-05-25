import os
WALLET_PW = os.environ.get("WALLET_PW", "")
WALLET_NAME = "bagbot"
# Auto-updated by taonow_sync at 2026-05-25 22:52 UTC
SUBNET_SETTINGS = {
    4: {
        'max_alpha': 30,
        'max_tao_per_buy': 0.1,
        'max_tao_per_sell': 0.1,
        'max_slippage_percent_per_buy': 1.0,
        'buy_lower': 0.04358382,
        'buy_upper': 0.06392294,
        'sell_lower': 0.06973412,
        'sell_upper': 0.10460118,
    },
    9: {
        'max_alpha': 30,
        'max_tao_per_buy': 0.1,
        'max_tao_per_sell': 0.1,
        'max_slippage_percent_per_buy': 1.0,
        'buy_lower': 0.02053944,
        'buy_upper': 0.03012451,
        'sell_lower': 0.0328631,
        'sell_upper': 0.04929465,
    },
    120: {
        'max_alpha': 30,
        'max_tao_per_buy': 0.1,
        'max_tao_per_sell': 0.1,
        'max_slippage_percent_per_buy': 1.0,
        'buy_lower': 0.04718745,
        'buy_upper': 0.06920826,
        'sell_lower': 0.07549992,
        'sell_upper': 0.11324989,
    },
}
