import httpx
import os
from dotenv import load_dotenv

load_dotenv()

class StancerClient:


    def __init__(self, username, password):
        self.base_url = os.getenv("API_BASE_URL")
        self.username = username
        self.password = password
        self.token = None
        self.client = httpx.Client(base_url=self.base_url)

    def authenticate(self):
        data = {
            "grant_type": "password",
            "username": self.username,
            "password": self.password,
            "scope": "stet"
        }

        headers = {
            "Content-Type": "application/x-www-form-urlencoded"
        }

        res = self.client.post("/oauth/token", data=data, headers=headers)

        if res.status_code == 200:
            self.token = res.json().get("access_token")
            self.client.headers.update({
                "Authorization": f"Bearer {self.token}"
            })
        else:
            raise Exception(f"Login failed: {res.status_code} - {res.text}")


    def get_identity(self):
        if not self.token:
            self.authenticate()

        res = self.client.get("/stet/identity")
        return res.json()

    def get_accounts(self):
        if not self.token:
            self.authenticate()

        res = self.client.get("/stet/account")
        return res.json()

    def get_balances(self, account_id):
        if not self.token:
            self.authenticate()

        res = self.client.get(f"/stet/account/{account_id}/balance")
        return res.json()

    def get_transactions(self, account_id):
        if not self.token:
            self.authenticate()

        res = self.client.get(f"/stet/account/{account_id}/transaction")
        return res.json()

    def close(self):
        self.client.close()
