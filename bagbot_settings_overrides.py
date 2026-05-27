import os
WALLET_PW = os.environ.get("WALLET_PW", "")
WALLET_NAME = "bagbot"
# Auto-updated by taonow_sync at 2026-05-27 08:32 UTC
SUBNET_SETTINGS = {
    4: {
        'max_alpha': 30,
        'max_tao_per_buy': 0.1,
        'max_tao_per_sell': 0.1,
        'max_slippage_percent_per_buy': 1.0,
        'buy_lower': 0.04282012,
        'buy_upper': 0.06280285,
        'sell_lower': 0.0685122,
        'sell_upper': 0.1027683,
    },
    9: {
        'max_alpha': 30,
        'max_tao_per_buy': 0.1,
        'max_tao_per_sell': 0.1,
        'max_slippage_percent_per_buy': 1.0,
        'buy_lower': 0.0220186,
        'buy_upper': 0.03229395,
        'sell_lower': 0.03522976,
        'sell_upper': 0.05284464,
    },
    120: {
        'max_alpha': 30,
        'max_tao_per_buy': 0.1,
        'max_tao_per_sell': 0.1,
        'max_slippage_percent_per_buy': 1.0,
        'buy_lower': 0.04686214,
        'buy_upper': 0.06873114,
        'sell_lower': 0.07497943,
        'sell_upper': 0.11246914,
    },
}
