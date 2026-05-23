import os
WALLET_PW = os.environ.get("WALLET_PW", "")
WALLET_NAME = "bagbot"
# Auto-updated by taonow_sync at 2026-05-23 19:36 UTC
SUBNET_SETTINGS = {
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
}
