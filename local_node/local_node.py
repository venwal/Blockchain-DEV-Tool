from web3 import Web3

def connect_to_node(rpc_url):
    w3 = Web3(Web3.HTTPProvider(rpc_url))
    if w3.isConnected():
        return f"Connected to Ethereum node at {rpc_url}"
    else:
        return "Failed to connect"

# Пример использования
rpc_url = "http://127.0.0.1:8545"
print(connect_to_node(rpc_url))
