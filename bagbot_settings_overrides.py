import os
WALLET_PW = os.environ.get("WALLET_PW", "")
WALLET_NAME = "bagbot"
# Auto-updated by taonow_sync at 2026-05-27 14:45 UTC
SUBNET_SETTINGS = {
    4: {
        'max_alpha': 30,
        'max_tao_per_buy': 0.1,
        'max_tao_per_sell': 0.1,
        'max_slippage_percent_per_buy': 1.0,
        'buy_lower': 0.04272156,
        'buy_upper': 0.06265829,
        'sell_lower': 0.0683545,
        'sell_upper': 0.10253175,
    },
    9: {
        'max_alpha': 30,
        'max_tao_per_buy': 0.1,
        'max_tao_per_sell': 0.1,
        'max_slippage_percent_per_buy': 1.0,
        'buy_lower': 0.02274917,
        'buy_upper': 0.03336545,
        'sell_lower': 0.03639868,
        'sell_upper': 0.05459801,
    },
    120: {
        'max_alpha': 30,
        'max_tao_per_buy': 0.1,
        'max_tao_per_sell': 0.1,
        'max_slippage_percent_per_buy': 1.0,
        'buy_lower': 0.0469798,
        'buy_upper': 0.06890371,
        'sell_lower': 0.07516768,
        'sell_upper': 0.11275152,
    },
}
