import os
from dotenv import load_dotenv, find_dotenv
import requests


load_dotenv(find_dotenv())
SHEETY_ENDPOINT = os.environ.get("SHEETY_ENDPOINT_FLIGHTS")
SHEETY_TOKEN = os.environ.get("SHEETY_TOKEN")



class DataManager:
    def __init__(self):
        #This class is responsible for talking to the Google Sheet.
        self.sheety_headers = {
            "Authorization": f"Bearer {SHEETY_TOKEN}"
        }

    def get_prices(self):
        response = requests.get(url=SHEETY_ENDPOINT,
                                 headers=self.sheety_headers)
        response.raise_for_status()
        self.sheet = response.json()["prices"]
        return self.sheet

    def update_lowest_price(self, row_id, new_price):
        row_url = f"{SHEETY_ENDPOINT}/{row_id}"
        params = {
            "price": {
                "lowestPrice" : new_price
            }
        }
        response = requests.put(url=row_url,
                                json=params,
                                 headers=self.sheety_headers)
        response.raise_for_status()
