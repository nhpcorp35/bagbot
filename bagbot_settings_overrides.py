import os
WALLET_PW = os.environ.get("WALLET_PW", "")
WALLET_NAME = "bagbot"
# Auto-updated by taonow_sync at 2026-05-27 06:29 UTC
SUBNET_SETTINGS = {
    4: {
        'max_alpha': 30,
        'max_tao_per_buy': 0.1,
        'max_tao_per_sell': 0.1,
        'max_slippage_percent_per_buy': 1.0,
        'buy_lower': 0.0428176,
        'buy_upper': 0.06279915,
        'sell_lower': 0.06850816,
        'sell_upper': 0.10276224,
    },
    9: {
        'max_alpha': 30,
        'max_tao_per_buy': 0.1,
        'max_tao_per_sell': 0.1,
        'max_slippage_percent_per_buy': 1.0,
        'buy_lower': 0.02201885,
        'buy_upper': 0.03229432,
        'sell_lower': 0.03523017,
        'sell_upper': 0.05284525,
    },
    120: {
        'max_alpha': 30,
        'max_tao_per_buy': 0.1,
        'max_tao_per_sell': 0.1,
        'max_slippage_percent_per_buy': 1.0,
        'buy_lower': 0.04686212,
        'buy_upper': 0.06873111,
        'sell_lower': 0.0749794,
        'sell_upper': 0.11246909,
    },
}
