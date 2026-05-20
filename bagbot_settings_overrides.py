import os
WALLET_PW = os.environ.get("WALLET_PW", "")
WALLET_NAME = "bagbot"
SUBNET_SETTINGS = {
    9: {
        'buy_lower':  0.018,    # buy aggressively if it pulls back ~40%
        'buy_upper':  0.030,    # start buying at/near current price
        'sell_lower': 0.045,    # start selling at ~50% above entry
        'sell_upper': 0.075,    # sell hard at ~2.5x
        'max_alpha':  25,
        'max_tao_per_buy': 0.10,
        'max_tao_per_sell': 0.10,
        'max_slippage_percent_per_buy': 0.5,
    },
    100: {
        'buy_lower':  0.008,    # buy aggressively near 30D low
        'buy_upper':  0.0135,   # start buying at/near current price
        'sell_lower': 0.020,    # start selling at ~50% above entry
        'sell_upper': 0.035,    # sell hard at ~2.5x
        'max_alpha':  15,       # small position — very thin pool
        'max_tao_per_buy': 0.10,
        'max_tao_per_sell': 0.10,
        'max_slippage_percent_per_buy': 1.5,
    },
    110: {
        'buy_lower':  0.003,    # buy aggressively if it drops ~70%
        'buy_upper':  0.0105,   # start buying at/near current price
        'sell_lower': 0.013,    # start selling at ~40% above entry
        'sell_upper': 0.025,    # sell hard near ~3x
        'max_alpha':  50,
        'max_tao_per_buy': 0.10,
        'max_tao_per_sell': 0.10,
        'max_slippage_percent_per_buy': 1.0,
    },
}
