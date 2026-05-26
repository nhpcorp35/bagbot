import os
WALLET_PW = os.environ.get("WALLET_PW", "")
WALLET_NAME = "bagbot"
# Auto-updated by taonow_sync at 2026-05-26 06:29 UTC
SUBNET_SETTINGS = {
    4: {
        'max_alpha': 30,
        'max_tao_per_buy': 0.1,
        'max_tao_per_sell': 0.1,
        'max_slippage_percent_per_buy': 1.0,
        'buy_lower': 0.04370572,
        'buy_upper': 0.06410173,
        'sell_lower': 0.06992916,
        'sell_upper': 0.10489373,
    },
    9: {
        'max_alpha': 30,
        'max_tao_per_buy': 0.1,
        'max_tao_per_sell': 0.1,
        'max_slippage_percent_per_buy': 1.0,
        'buy_lower': 0.02059052,
        'buy_upper': 0.03019943,
        'sell_lower': 0.03294483,
        'sell_upper': 0.04941725,
    },
    120: {
        'max_alpha': 30,
        'max_tao_per_buy': 0.1,
        'max_tao_per_sell': 0.1,
        'max_slippage_percent_per_buy': 1.0,
        'buy_lower': 0.0475401,
        'buy_upper': 0.06972548,
        'sell_lower': 0.07606416,
        'sell_upper': 0.11409623,
    },
}
