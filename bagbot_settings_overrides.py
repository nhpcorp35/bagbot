import os
WALLET_PW = os.environ.get("WALLET_PW", "")
WALLET_NAME = "bagbot"
SUBNET_SETTINGS = {
    4: {
        'buy_lower': 0.04205802,
        'buy_upper': 0.0616851,
        'max_alpha': 30,
        'max_slippage_percent_per_buy': 1,
        'max_tao_per_buy': 0.1,
        'max_tao_per_sell': 0.1,
        'sell_lower': 0.06729283,
        'sell_upper': 0.10093925,
    },
    9: {
        'buy_lower': 0.02274917,
        'buy_upper': 0.03336545,
        'max_alpha': 30,
        'max_slippage_percent_per_buy': 1,
        'max_tao_per_buy': 0.1,
        'max_tao_per_sell': 0.1,
        'sell_lower': 0.04413,
        'sell_upper': 0.0735,
    },
    62: {
        'buy_lower': 0.01246563,
        'buy_upper': 0.01828293,
        'max_alpha': 30,
        'max_slippage_percent_per_buy': 1,
        'max_tao_per_buy': 0.1,
        'max_tao_per_sell': 0.1,
        'sell_lower': 0.01994501,
        'sell_upper': 0.02991752,
    },
    64: {
        'buy_lower': 0.05176,
        'buy_upper': 0.07591,
        'max_alpha': 30,
        'sell_lower': 0.08281,
        'sell_upper': 0.12422,
    },
    120: {
        'buy_lower': 0.04679293,
        'buy_upper': 0.06862963,
        'max_alpha': 30,
        'max_slippage_percent_per_buy': 1,
        'max_tao_per_buy': 0.1,
        'max_tao_per_sell': 0.1,
        'sell_lower': 0.07486868,
        'sell_upper': 0.11230303,
    },
}
