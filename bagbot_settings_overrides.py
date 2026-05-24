import os
WALLET_PW = os.environ.get("WALLET_PW", "")
WALLET_NAME = "bagbot"
# Auto-updated by taonow_sync at 2026-05-24 02:46 UTC
SUBNET_SETTINGS = {
    4: {
        'max_alpha': 30,
        'max_tao_per_buy': 0.1,
        'max_tao_per_sell': 0.1,
        'max_slippage_percent_per_buy': 1.0,
        'buy_lower': 0.03356655,
        'buy_upper': 0.05706314,
        'sell_lower': 0.07832196,
        'sell_upper': 0.13986064,
    },
    9: {
        'max_alpha': 30,
        'max_tao_per_buy': 0.1,
        'max_tao_per_sell': 0.1,
        'max_slippage_percent_per_buy': 1.0,
        'buy_lower': 0.01575886,
        'buy_upper': 0.02679006,
        'sell_lower': 0.03677066,
        'sell_upper': 0.0656619,
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
        'buy_lower': 0.03863422,
        'buy_upper': 0.06567818,
        'sell_lower': 0.09014652,
        'sell_upper': 0.16097593,
    },
}
