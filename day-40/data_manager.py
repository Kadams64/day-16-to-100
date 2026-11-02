import os
from pprint import pprint

import requests
from dotenv import load_dotenv, find_dotenv

# Load environment variables from .env file
load_dotenv(find_dotenv())

SHEETY_PRICES_ENDPOINT = os.environ["SHEETY_PRICES_ENDPOINT"]
SHEETY_USERS_ENDPOINT = os.environ.get("SHEETY_ENDPOINT_USERS")
SHEETY_TOKEN = os.environ.get("SHEETY_TOKEN")

class DataManager:

    def __init__(self):
        self.sheety_headers = {
            "Authorization": f"Bearer {SHEETY_TOKEN}"
        }
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=SHEETY_PRICES_ENDPOINT,
                                headers=self.sheety_headers)
        response.raise_for_status()
        sheet = response.json()["prices"]
        return sheet

    # ==================== Updated the price in the spreadsheet ====================

    def update_lowest_price(self, row_id, new_price):
        new_data = {
            "price": {
                "lowestPrice": new_price
            }
        }
        requests.put(
            url=f"{SHEETY_PRICES_ENDPOINT}/{row_id}",
            json=new_data,
            headers=self.sheety_headers
        )
    def get_customer_emails(self):
        response = requests.get(url=SHEETY_USERS_ENDPOINT,
                                headers=self.sheety_headers)
        response.raise_for_status()
        sheet = response.json()["users"]
        return sheet
