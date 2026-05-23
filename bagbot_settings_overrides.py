import os
WALLET_PW = os.environ.get("WALLET_PW", "")
WALLET_NAME = "bagbot"
# Auto-updated by taonow_sync at 2026-05-23 09:52 UTC
SUBNET_SETTINGS = {
    4: {
        'max_alpha': 30,
        'max_tao_per_buy': 0.1,
        'max_tao_per_sell': 0.1,
        'max_slippage_percent_per_buy': 1.0,
        'buy_lower': 0.03350944,
        'buy_upper': 0.05696605,
        'sell_lower': 0.0781887,
        'sell_upper': 0.13962267,
    },
    9: {
        'max_alpha': 30,
        'max_tao_per_buy': 0.1,
        'max_tao_per_sell': 0.1,
        'max_slippage_percent_per_buy': 1.0,
        'buy_lower': 0.01520542,
        'buy_upper': 0.02584922,
        'sell_lower': 0.03547932,
        'sell_upper': 0.06335592,
    },
    100: {
        'buy_lower': 0.00649103,
        'buy_upper': 0.0,
        'sell_lower': 0.01233296,
        'sell_upper': 0.01947309,
        'max_alpha': 1,
        'max_tao_per_buy': 0.0,
        'max_tao_per_sell': 0.1,
        'max_slippage_percent_per_buy': 1.0,
    },
    120: {
        'max_alpha': 30,
        'max_tao_per_buy': 0.1,
        'max_tao_per_sell': 0.1,
        'max_slippage_percent_per_buy': 1.0,
        'buy_lower': 0.03748184,
        'buy_upper': 0.06371912,
        'sell_lower': 0.08745762,
        'sell_upper': 0.15617432,
    },
}
