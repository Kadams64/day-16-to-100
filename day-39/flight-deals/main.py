from data_manager import DataManager
from flight_search import FlightSearch
import flight_data as fd
from pprint import pprint
import requests_cache
from datetime import datetime, timedelta
import os
from dotenv import load_dotenv

# Cache all requests for 10 minutes except serpapi.com which should be cached
# for one hour
requests_cache.install_cache(
    "flights_cache",
    expire_after=300,
    urls_expire_after={
        "serpapi.com": 3600,
    },
)

# This file will need to use the DataManager,FlightSearch, FlightData,
# NotificationManager classes to achieve the program requirements.
dm = DataManager()
flights = FlightSearch()

sheet_data = dm.get_prices()

today = datetime.now()
six_months_hence = today + timedelta(days=182)

for destination in sheet_data:
    # destination = sheet_data[1]
    destination_iata = destination["iataCode"]
    print(destination_iata)
    flight_json = flights.check_flights(origin_city="YVR", destination_city=destination_iata,
                                        from_time=today, to_time=six_months_hence)
    pprint(flight_json)
    cheapest_flight = fd.find_cheapest_flight(flight_json, six_months_hence)
    # print(f"origin= {cheapest_flight.origin_airport}; destination={cheapest_flight.destination_airport}")
    if (cheapest_flight.price != "N/A" and
            int(cheapest_flight.price) < int(destination["lowestPrice"])):
        print("New lowest price found!")
        dm.update_lowest_price(row_id=destination["id"], new_price=cheapest_flight.price)