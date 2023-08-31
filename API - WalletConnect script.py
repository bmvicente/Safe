import requests
import json

def count_wallet_connect_transactions():
    url = "https://safe-transaction-mainnet.safe.global/api/v1/safes/0xBbA4C8eB57DF16c4CfAbe4e9A3Ab697A3e0C65D8/multisig-transactions/"
    
    response = requests.get(url)
    
    transactions = response.json()['results']
    
    wallet_connect_count = 0
    
    for tx in transactions:
        try:
            origin_data = json.loads(tx['origin'])
            if "WalletConnect" in origin_data.get("name", ""):
                wallet_connect_count += 1
        except json.JSONDecodeError:
            continue
            
    print(f"Number of WalletConnect txs: {wallet_connect_count}")

if __name__ == "__main__":
    count_wallet_connect_transactions()
