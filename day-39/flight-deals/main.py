from data_manager import DataManager
from flight_search import FlightSearch
from pprint import pprint
import requests_cache
from datetime import datetime, timedelta
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
flights = FlightSearch()

sheet_data = dm.get_prices()
pprint(sheet_data)
today = datetime.now()
six_months_hence = today + timedelta(days=182)
flight_json = flights.check_flights(origin_city="YVR", destination_city="JFK",
                                    from_time=today, to_time=six_months_hence)

# some logic to add the two lists of flights from the dictionary together

flights_other = flight_json.get("other_flights", [])

flights_best = flight_json.get("best_flights", [])
flights_to_process = (flights_best) + (flights_other)

# end result in flights_to_process is a combined list without any errors on
# missing keys
print(flights_best)

print(flights_to_process)