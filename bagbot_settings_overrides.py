import os
WALLET_PW = os.environ.get("WALLET_PW", "")
WALLET_NAME = "bagbot"
# Auto-updated by taonow_sync at 2026-05-25 02:03 UTC
SUBNET_SETTINGS = {
    4: {
        'max_alpha': 30,
        'max_tao_per_buy': 0.1,
        'max_tao_per_sell': 0.1,
        'max_slippage_percent_per_buy': 1.0,
        'buy_lower': 0.03412644,
        'buy_upper': 0.05801495,
        'sell_lower': 0.07962836,
        'sell_upper': 0.14219351,
    },
    9: {
        'max_alpha': 30,
        'max_tao_per_buy': 0.1,
        'max_tao_per_sell': 0.1,
        'max_slippage_percent_per_buy': 1.0,
        'buy_lower': 0.01641499,
        'buy_upper': 0.02790548,
        'sell_lower': 0.03830163,
        'sell_upper': 0.06839578,
    },
    62: {
        'max_alpha': 30,
        'max_tao_per_buy': 0.1,
        'max_tao_per_sell': 0.1,
        'max_slippage_percent_per_buy': 1.0,
        'buy_lower': 0.01058454,
        'buy_upper': 0.01799372,
        'sell_lower': 0.02469726,
        'sell_upper': 0.04410224,
    },
}
