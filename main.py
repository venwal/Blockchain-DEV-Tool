from config import RPC_ENDPOINTS, DEFAULT_TOKEN
from functions import connect_to_blockchain, get_balance, send_transaction, generate_smart_contract

def main():
    print("Welcome to the Blockchain Dev Tool!")
    print("Available networks:")
    for network in RPC_ENDPOINTS.keys():
        print(f"- {network}")
    
    # Network selection
    network = input("Enter the blockchain network you want to connect to: ").lower()
    if network not in RPC_ENDPOINTS:
        print("Unsupported network.")
        return

    # Connecting to blockchain
    rpc_url = RPC_ENDPOINTS[network]
    web3 = connect_to_blockchain(rpc_url)
    if not web3:
        return

    # Main menu
    while True:
        print("\nMain Menu:")
        print("1. Check account balance")
        print("2. Send a transaction")
        print("3. Generate a smart contract")
        print("4. Exit")
        choice = input("Select an option: ")

        if choice == "1":
            address = input("Enter the address to check balance: ")
            balance = get_balance(web3, address)
            if balance is not None:
                print(f"Balance of {address}: {balance} ETH")
        
        elif choice == "2":
            private_key = input("Enter your private key: ")
            to_address = input("Enter recipient's address: ")
            amount = float(input("Enter the amount to send (ETH): "))
            tx_hash = send_transaction(web3, private_key, to_address, amount)
            if tx_hash:
                print(f"Transaction hash: {tx_hash}")
        
        elif choice == "3":
            name = input(f"Enter token name (default: {DEFAULT_TOKEN['name']}): ") or DEFAULT_TOKEN["name"]
            symbol = input(f"Enter token symbol (default: {DEFAULT_TOKEN['symbol']}): ") or DEFAULT_TOKEN["symbol"]
            total_supply = int(input(f"Enter total supply (default: {DEFAULT_TOKEN['total_supply']}): ") or DEFAULT_TOKEN["total_supply"])
            contract = generate_smart_contract(name, symbol, total_supply)
            print("\nGenerated Smart Contract:")
            print(contract)

        elif choice == "4":
            print("Exiting program. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
