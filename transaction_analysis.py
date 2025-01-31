from web3 import Web3

def analyze_transactions(rpc_url, block_number):
    w3 = Web3(Web3.HTTPProvider(rpc_url))
    if not w3.isConnected():
        return "Failed to connect to node"

    block = w3.eth.get_block(block_number, full_transactions=True)
    tx_data = []
    for tx in block.transactions:
        tx_data.append({
            "from": tx["from"],
            "to": tx["to"],
            "value": w3.fromWei(tx["value"], "ether"),
        })
    return tx_data

# Example of use
rpc_url = "http://127.0.0.1:8545"
print(analyze_transactions(rpc_url, 1))  # Analyze the 1st block
