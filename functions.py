from web3 import Web3

# Connecting to the blockchain via RPC
def connect_to_blockchain(rpc_url):
    try:
        web3 = Web3(Web3.HTTPProvider(rpc_url))
        if web3.is_connected():
            print(f"Successfully connected to blockchain at {rpc_url}")
            return web3
        else:
            print("Failed to connect to blockchain.")
            return None
    except Exception as e:
        print(f"Error connecting to blockchain: {e}")
        return None

# Address balance check
def get_balance(web3, address):
    try:
        balance = web3.eth.get_balance(address)
        return web3.from_wei(balance, "ether")
    except Exception as e:
        print(f"Error retrieving balance for {address}: {e}")
        return None

# Sending a transaction
def send_transaction(web3, private_key, to_address, amount):
    try:
        account = web3.eth.account.from_key(private_key)
        nonce = web3.eth.get_transaction_count(account.address)
        tx = {
            "nonce": nonce,
            "to": to_address,
            "value": web3.to_wei(amount, "ether"),
            "gas": 21000,
            "gasPrice": web3.to_wei("50", "gwei"),
            "chainId": web3.eth.chain_id,
        }
        signed_tx = web3.eth.account.sign_transaction(tx, private_key)
        tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
        print(f"Transaction sent! Tx hash: {tx_hash.hex()}")
        return tx_hash.hex()
    except Exception as e:
        print(f"Error sending transaction: {e}")
        return None

# Smart contract generation
def generate_smart_contract(name, symbol, total_supply):
    return f"""
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract {name} {{
    string public name = "{name}";
    string public symbol = "{symbol}";
    uint256 public totalSupply = {total_supply};

    mapping(address => uint256) public balances;

    constructor() {{
        balances[msg.sender] = totalSupply;
    }}

    function transfer(address to, uint256 amount) public returns (bool) {{
        require(balances[msg.sender] >= amount, "Not enough tokens");
        balances[msg.sender] -= amount;
        balances[to] += amount;
        return true;
    }}
}}
"""

