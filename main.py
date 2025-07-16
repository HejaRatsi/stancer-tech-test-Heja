from stancer.client import StancerClient

if __name__ == '__main__':
    print("Starting Stancer DSP2 client test")

    client = StancerClient("mdupuis", "111111")

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
