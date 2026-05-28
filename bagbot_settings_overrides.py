import os
WALLET_PW = os.environ.get("WALLET_PW", "")
WALLET_NAME = "bagbot"
SUBNET_SETTINGS = {
    9: {
        'buy_lower': 0.02274917,
        'buy_upper': 0.03336545,
        'max_alpha': 30,
        'max_slippage_percent_per_buy': 1,
        'max_tao_per_buy': 0.1,
        'max_tao_per_sell': 0.1,
        'sell_lower': 0.03639868,
        'sell_upper': 0.05459801,
    },
    64: {
        'buy_lower': 0.05176,
        'buy_upper': 0.07591,
        'sell_lower': 0.08281,
        'sell_upper': 0.12422,
        'max_alpha': 30,
    },
    120: {
        'buy_lower': 0.0469798,
        'buy_upper': 0.06890371,
        'max_alpha': 30,
        'max_slippage_percent_per_buy': 1,
        'max_tao_per_buy': 0.1,
        'max_tao_per_sell': 0.1,
        'sell_lower': 0.07516768,
        'sell_upper': 0.11275152,
    },
}
