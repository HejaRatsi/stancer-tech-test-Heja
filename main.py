from stancer.client import StancerClient
import os
from dotenv import load_dotenv

load_dotenv(override=True) #sinon utilisation des variables du systeme

def main():
    print("Starting Stancer DSP2 client test")

    username = os.getenv("USERNAME")
    password = os.getenv("PASSWORD")

    print("USERNAME:", username)
    print("PASSWORD:", password)

    client = StancerClient(username, password)

    try:
        identity = client.get_identity()
        print("Identity:", identity)

        accounts = client.get_accounts()
        print("Accounts:", accounts)

        for account in accounts:
            account_id = account["id"]
            balance = client.get_balances(account_id)
            print(f"Balance for {account_id}:", balance)

            transactions = client.get_transactions(account_id)
            print(f"Transactions for {account_id}:", transactions)

    finally:
        client.close()
        print("Client closed")

if __name__ == '__main__':
    main()
