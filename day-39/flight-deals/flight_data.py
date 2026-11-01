import datetime


class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self, price, origin_airport, destination_airport,
                  departure_date, return_date):
        self.price = price
        self.origin_airport = origin_airport
        self.destination_airport = destination_airport
        self.depart_date = departure_date
        self.return_date = return_date

def find_cheapest_flight(data, return_date: datetime.datetime):
    # some logic to add the two lists of flights from the dictionary together

    flights_other = data.get("other_flights", [])

    flights_best = data.get("best_flights", [])
    flights_to_process = (flights_best) + (flights_other)
    if len(flights_to_process) == 0:
        print("No flight data to process.")
        return FlightData("N/A", "N/A", "N/A",
                          "N/A", "N/A")
    # end result in flights_to_process is a combined list without any errors on
    # missing keys

    first_flight = flights_to_process[0]
    lowest_price = first_flight["price"]
    origin = first_flight["flights"][0]["departure_airport"]["id"]
    destination = first_flight["flights"][-1]["arrival_airport"]["id"]
    out_date = first_flight["flights"][0]["departure_airport"]["time"].split(" ")[0]
    print(lowest_price)

    cheapest_flight = FlightData(lowest_price, origin, destination, out_date, return_date)
    for flight in flights_to_process:
        # Exception handling - json has data but flight is missing 'price'. Skip.
        try:
            price = flight["price"]
        except KeyError:
            print("--- No price available for flight. ---")
            continue
        if price < lowest_price:
            lowest_price = price
            origin = flight["flights"][0]["departure_airport"]["id"]
            destination = flight["flights"][-1]["arrival_airport"]["id"]
            out_date = flight["flights"][0]["departure_airport"]["time"].split(" ")[0]
            cheapest_flight = FlightData(lowest_price, origin, destination, out_date, return_date)
            print(f"Lowest price to {destination} is CAD {lowest_price}")

    return cheapest_flight

