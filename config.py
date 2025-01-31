# RPC addresses to connect to blockchain nodes
RPC_ENDPOINTS = {
    "ethereum": "http://127.0.0.1:8545",
    "binance_smart_chain": "https://bsc-dataseed.binance.org/",
    "polygon": "https://polygon-rpc.com/"
}

# Network parameters
NETWORK_CONFIG = {
    "ethereum": {
        "chain_id": 1,
        "symbol": "ETH",
        "block_explorer": "https://etherscan.io"
    },
    "binance_smart_chain": {
        "chain_id": 56,
        "symbol": "BNB",
        "block_explorer": "https://bscscan.com"
    },
    "polygon": {
        "chain_id": 137,
        "symbol": "MATIC",
        "block_explorer": "https://polygonscan.com"
    }
}

# API keys (if you need to use external services)
API_KEYS = {
    "etherscan": "YOUR_ETHERSCAN_API_KEY"
}

# Token settings
DEFAULT_TOKEN = {
    "name": "MyToken",
    "symbol": "MTK",
    "total_supply": 1000000
}
