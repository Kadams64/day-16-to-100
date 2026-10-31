from data_manager import DataManager
from pprint import pprint
import requests_cache
import os
from dotenv import load_dotenv

# Cache all requests for 10 minutes except serpapi.com which should be cached
# for one hour
requests_cache.install_cache(
    "flights_cache",
    expire_after=600,
    urls_expire_after={
        "serpapi.com": 3600,
    },
)

# This file will need to use the DataManager,FlightSearch, FlightData,
# NotificationManager classes to achieve the program requirements.
dm = DataManager()

sheet_data = dm.get_prices()
pprint(sheet_data)