import os
import pprint

import requests
from dotenv import load_dotenv
import requests_cache

load_dotenv()

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.data = []
        load_dotenv()
        self.auth_token = os.getenv("SHEETY_BASIC_AUTH_TOKEN")
        self.prices_url = os.getenv("PRICES_SHEET_DATA_URL")
        self.users_url = os.getenv("USERS_DATA_URL")

    def get_data(self):
        with requests_cache.disabled():
            response = requests.get(url=str(self.prices_url), headers={'Authorization': f'Basic {self.auth_token}'})
            response.raise_for_status()
            self.data = response.json()["prices"]
            return self.data

    def update_lowest_price(self, row_data, new_price):
        row_id = row_data["id"]
        data = {
            "price": {
                "cityName": row_data["cityName"],
                "iataCode": row_data["iataCode"],
                "id": row_id,
                "lowestPrice": new_price
            }
        }

        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Basic {self.auth_token}"
        }

        with requests_cache.disabled():
            response = requests.put(url=self.prices_url+f"/{row_id}",
                                    headers=headers,
                                    json=data)
            if response.status_code == 200:
                print(f"Update successful for {row_id}")
            else:
                print(f"Update failed for {row_id}, error code: {response.status_code}")
                print(response.text)

    def get_customers_emails(self):
        emails = []
        response = requests.get(url=str(self.users_url), headers={'Authorization': f'Basic {self.auth_token}'})
        if response.status_code == 200:
            data = response.json()["users"]
            for row in data:
                emails.append(row["whatIsYourEmail?"])
            return emails
        else:
            print(f"Fetching users email failed with error {response.text}")
            return None
