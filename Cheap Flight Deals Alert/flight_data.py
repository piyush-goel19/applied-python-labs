
def find_cheapest_flight(search_data, return_date):
    if search_data is None or (len(search_data["other_flights"]) == 0 and len(search_data["best_flights"]) == 0):
        return None

    all_flights = search_data["other_flights"]
    if "best_flights" in search_data:
        all_flights += search_data["best_flights"]

    print(all_flights)

    cheapest_flight = None

    for flight in all_flights:
        print(flight)
        if "price" not in flight:
            continue
        price = flight["price"]
        departure_airport = flight["flights"][0]["departure_airport"]["id"]
        departure_date = flight["flights"][0]["departure_airport"]["time"].split(" ")[0]
        arrival_airport = flight["flights"][-1]["arrival_airport"]["id"]
        stopovers = len(flight["flights"]) - 1

        flight_data = FlightData(price, departure_airport, arrival_airport, departure_date, return_date, stopovers)

        if cheapest_flight is None or cheapest_flight.price > flight_data.price:
            cheapest_flight = flight_data

    return cheapest_flight


class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self, price, departure_airport,
                arrival_airport, out_date, return_date, stopovers):
        self.price = price
        self.departure_airport = departure_airport
        self.arrival_airport = arrival_airport
        self.out_date = out_date
        self.return_date = return_date
        self.stopovers = stopovers
