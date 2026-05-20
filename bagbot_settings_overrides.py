import os
WALLET_PW = os.environ.get("WALLET_PW", "")
WALLET_NAME = "bagbot"
SUBNET_SETTINGS = {
    6: {
        'buy_lower':  0.002,    # buy aggressively near 30D low
        'buy_upper':  0.0042,   # start buying at/near current price
        'sell_lower': 0.007,    # start selling at ~70% above entry
        'sell_upper': 0.012,    # sell hard near 30D high
        'max_alpha':  100,      # reduced to share capital with SN110
        'max_tao_per_buy': 0.15,
        'max_tao_per_sell': 0.15,
        'max_slippage_percent_per_buy': 0.5,
    },
    110: {
        'buy_lower':  0.003,    # buy aggressively if it drops ~70%
        'buy_upper':  0.0105,   # raised to chase current price
        'sell_lower': 0.013,    # start selling at ~40% above entry
        'sell_upper': 0.025,    # sell hard near ~3x
        'max_alpha':  50,       # smaller position, more volatile subnet
        'max_tao_per_buy': 0.15,
        'max_tao_per_sell': 0.15,
        'max_slippage_percent_per_buy': 1.0,
    },
}
