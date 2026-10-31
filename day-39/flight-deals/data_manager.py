import os
from dotenv import load_dotenv
import requests



load_dotenv("/Users/kellyadams/PycharmProjects/day-16-to-100/.env")
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