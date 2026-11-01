import datetime


class FlightData:
    #This class is responsible for structuring the flight data.
    def __index__(self, price, origin_airport, destination_airport,
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

    # end result in flights_to_process is a combined list without any errors on
    # missing keys

    print(len(flights_to_process))
    for flight in flights_to_process:
        # cheating now looking at the solution because of frustrations
        # in the house
        pass

