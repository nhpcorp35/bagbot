import os
WALLET_PW = os.environ.get("WALLET_PW", "")
WALLET_NAME = "bagbot"
SUBNET_SETTINGS = {
    6: {
        'buy_lower':  0.002,    # buy aggressively near 30D low
        'buy_upper':  0.0042,   # start buying at/near current price
        'sell_lower': 0.007,    # start selling at ~70% above entry
        'sell_upper': 0.012,    # sell hard near 30D high
        'max_alpha':  200,
        'max_slippage_percent_per_buy': 0.5,
    },
}
