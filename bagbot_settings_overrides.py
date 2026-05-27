import os
WALLET_PW = os.environ.get("WALLET_PW", "")
WALLET_NAME = "bagbot"
# Auto-updated by taonow_sync at 2026-05-27 03:54 UTC
SUBNET_SETTINGS = {
    4: {
        'max_alpha': 30,
        'max_tao_per_buy': 0.1,
        'max_tao_per_sell': 0.1,
        'max_slippage_percent_per_buy': 1.0,
        'buy_lower': 0.0429938,
        'buy_upper': 0.06305758,
        'sell_lower': 0.06879008,
        'sell_upper': 0.10318513,
    },
    9: {
        'max_alpha': 30,
        'max_tao_per_buy': 0.1,
        'max_tao_per_sell': 0.1,
        'max_slippage_percent_per_buy': 1.0,
        'buy_lower': 0.02200019,
        'buy_upper': 0.03226694,
        'sell_lower': 0.0352003,
        'sell_upper': 0.05280045,
    },
    120: {
        'max_alpha': 30,
        'max_tao_per_buy': 0.1,
        'max_tao_per_sell': 0.1,
        'max_slippage_percent_per_buy': 1.0,
        'buy_lower': 0.04686351,
        'buy_upper': 0.06873315,
        'sell_lower': 0.07498161,
        'sell_upper': 0.11247242,
    },
}
