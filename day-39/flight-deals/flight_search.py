import datetime
import os
from dotenv import load_dotenv, find_dotenv
import requests

load_dotenv(find_dotenv())

class FlightSearch:
    # This class is responsible for talking to the Flight Search API.

    """I have the SerpAPI site set up and caching set for 60 minutes"""
    def __init__(self):
        self._api_key = os.environ.get("SERP_API_KEY")

    def check_flights(self, origin_city, destination_city,
                      from_time: datetime.datetime, to_time:datetime.datetime):
        parameters = {
            "engine": "google_flights",
            "departure_id": origin_city,
            "arrival_id": destination_city,
            "outbound_date": from_time.strftime("%Y-%m-%d"),
            "return_date": to_time.strftime("%Y-%m-%d"),
            "type": "1",
            "adults": "1",
            "currency": "CAD",
            "api_key": self._api_key,
        }
        self._serpapi_url = "https://serpapi.com/search.json"
        response = requests.get(url=self._serpapi_url, params=parameters)
        response.raise_for_status()
        self.json = response.json()
        return self.json