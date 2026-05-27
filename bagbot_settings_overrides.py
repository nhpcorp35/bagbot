import os
WALLET_PW = os.environ.get("WALLET_PW", "")
WALLET_NAME = "bagbot"
# Auto-updated by taonow_sync at 2026-05-27 11:19 UTC
SUBNET_SETTINGS = {
    4: {
        'max_alpha': 30,
        'max_tao_per_buy': 0.1,
        'max_tao_per_sell': 0.1,
        'max_slippage_percent_per_buy': 1.0,
        'buy_lower': 0.04275116,
        'buy_upper': 0.06270171,
        'sell_lower': 0.06840186,
        'sell_upper': 0.10260279,
    },
    9: {
        'max_alpha': 30,
        'max_tao_per_buy': 0.1,
        'max_tao_per_sell': 0.1,
        'max_slippage_percent_per_buy': 1.0,
        'buy_lower': 0.0220877,
        'buy_upper': 0.03239529,
        'sell_lower': 0.03534032,
        'sell_upper': 0.05301048,
    },
    120: {
        'max_alpha': 30,
        'max_tao_per_buy': 0.1,
        'max_tao_per_sell': 0.1,
        'max_slippage_percent_per_buy': 1.0,
        'buy_lower': 0.04678471,
        'buy_upper': 0.06861757,
        'sell_lower': 0.07485553,
        'sell_upper': 0.1122833,
    },
}
