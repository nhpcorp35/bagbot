import os
WALLET_PW = os.environ.get("WALLET_PW", "")
WALLET_NAME = "bagbot"
# Auto-updated by taonow_sync at 2026-05-27 05:27 UTC
SUBNET_SETTINGS = {
    4: {
        'max_alpha': 30,
        'max_tao_per_buy': 0.1,
        'max_tao_per_sell': 0.1,
        'max_slippage_percent_per_buy': 1.0,
        'buy_lower': 0.04299732,
        'buy_upper': 0.06306274,
        'sell_lower': 0.06879572,
        'sell_upper': 0.10319358,
    },
    9: {
        'max_alpha': 30,
        'max_tao_per_buy': 0.1,
        'max_tao_per_sell': 0.1,
        'max_slippage_percent_per_buy': 1.0,
        'buy_lower': 0.0220004,
        'buy_upper': 0.03226726,
        'sell_lower': 0.03520064,
        'sell_upper': 0.05280097,
    },
    120: {
        'max_alpha': 30,
        'max_tao_per_buy': 0.1,
        'max_tao_per_sell': 0.1,
        'max_slippage_percent_per_buy': 1.0,
        'buy_lower': 0.0468635,
        'buy_upper': 0.06873313,
        'sell_lower': 0.0749816,
        'sell_upper': 0.11247239,
    },
}
