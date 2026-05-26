import os
WALLET_PW = os.environ.get("WALLET_PW", "")
WALLET_NAME = "bagbot"
# Auto-updated by taonow_sync at 2026-05-26 21:07 UTC
SUBNET_SETTINGS = {
    4: {
        'buy_lower': 0.02890778,
        'buy_upper': 0.0,
        'sell_lower': 0.05492478,
        'sell_upper': 0.08672334,
        'max_alpha': 1,
        'max_tao_per_buy': 0.0,
        'max_tao_per_sell': 0.1,
        'max_slippage_percent_per_buy': 1.0,
    },
    9: {
        'buy_lower': 0.01382673,
        'buy_upper': 0.0,
        'sell_lower': 0.02627079,
        'sell_upper': 0.04148019,
        'max_alpha': 1,
        'max_tao_per_buy': 0.0,
        'max_tao_per_sell': 0.1,
        'max_slippage_percent_per_buy': 1.0,
    },
    120: {
        'buy_lower': 0.03118736,
        'buy_upper': 0.0,
        'sell_lower': 0.05925598,
        'sell_upper': 0.09356208,
        'max_alpha': 1,
        'max_tao_per_buy': 0.0,
        'max_tao_per_sell': 0.1,
        'max_slippage_percent_per_buy': 1.0,
    },
}
