import os
WALLET_PW = os.environ.get("WALLET_PW", "")
WALLET_NAME = "bagbot"
# Auto-updated by taonow_sync at 2026-05-27 12:23 UTC
SUBNET_SETTINGS = {
    4: {
        'max_alpha': 30,
        'max_tao_per_buy': 0.1,
        'max_tao_per_sell': 0.1,
        'max_slippage_percent_per_buy': 1.0,
        'buy_lower': 0.04272157,
        'buy_upper': 0.0626583,
        'sell_lower': 0.0683545,
        'sell_upper': 0.10253176,
    },
    9: {
        'max_alpha': 30,
        'max_tao_per_buy': 0.1,
        'max_tao_per_sell': 0.1,
        'max_slippage_percent_per_buy': 1.0,
        'buy_lower': 0.02273645,
        'buy_upper': 0.03334679,
        'sell_lower': 0.03637832,
        'sell_upper': 0.05456748,
    },
    120: {
        'max_alpha': 30,
        'max_tao_per_buy': 0.1,
        'max_tao_per_sell': 0.1,
        'max_slippage_percent_per_buy': 1.0,
        'buy_lower': 0.0469798,
        'buy_upper': 0.06890371,
        'sell_lower': 0.07516769,
        'sell_upper': 0.11275153,
    },
}
