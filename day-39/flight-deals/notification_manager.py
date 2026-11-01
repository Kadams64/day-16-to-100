import requests
import os
from twilio.rest import Client
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")
ACCOUNT_SID = os.environ.get("TWILIO_SID")

FROM_PHONE = os.environ.get("TWILIO_PHONE")
MY_PHONE = os.environ.get("MY_PHONE")

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self, price: float, depart:str, arrival: str, outbound, inbound):
        self.price = price
        self.depart = depart
        self.arrival = arrival
        self.outbound_date = outbound
        self.inbound_date = inbound

    def send_message(self) -> bool:
        print(f"{self.price}; {self.depart}; {self.arrival}")

        client = Client(ACCOUNT_SID, AUTH_TOKEN)
        message = client.messages.create(
            body=f"Low Price Alert! Only ${self.price} to fly "
                 f"from {self.depart} to {self.arrival} "
                 f"on {self.outbound_date} until {self.inbound_date}",
            from_=FROM_PHONE,
            to=MY_PHONE
        )

        return True