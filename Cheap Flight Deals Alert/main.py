# Functional Requirements
# 1. Use Sheety to read google doc. Sheet contins airport IATA codes each destination city

# 2. Use serpAPI to check for cheapest flight from tomorrow to 6 months later for all the
# cities in the Google Sheet.

# 3. If the price is lower than the lowest price listed in the Google Sheet then send an
# Email to your own emailId. The SMS (or WhatsApp message) should include the departure
# airport IATA code, destination airport IATA code, flight price and flight dates.
# Sample msg - "Low Price Alert! Only ₹x.xx to fly from DEL to KUL, on {date} till {endDate}."

import data_manager as dm
import flight_search as fs
import flight_data as fd
import notification_manager as n_mn
from pprint import pprint
import requests_cache
from datetime import datetime, timedelta

requests_cache.install_cache('flights-cache', expire_after=3600)
ORIGIN_CITY_CODE = 'DEL'

tomorrow = (datetime.now() + timedelta(days=1)).date()
day_six_months_from_today = (datetime.now() + timedelta(days=180)).date()

data_manager = dm.DataManager()
dest_prices_data = data_manager.get_data()
pprint(dest_prices_data)
users_email_data = data_manager.get_customers_emails()
print(users_email_data)

flight_search = fs.FlightSearch()
flights_data = {}
notification = n_mn.NotificationManager()

for price_data in dest_prices_data:
    dest_city = price_data["iataCode"]
    flights_data = flight_search.check_flights(origin_city_code=ORIGIN_CITY_CODE,
                                               destination_city_code=dest_city,
                                               from_date=tomorrow, to_date=day_six_months_from_today)
    if flights_data is None:
        print(f"No direct flights to {dest_city} found. Looking for indirect flights...")
        flights_data = flight_search.check_flights(origin_city_code=ORIGIN_CITY_CODE,
                                               destination_city_code=dest_city,
                                               from_date=tomorrow, to_date=day_six_months_from_today, is_direct=False)

    cheapest_flight = fd.find_cheapest_flight(flights_data, day_six_months_from_today)
    if cheapest_flight is None:
        print("No cheapest flight found.")
    else:
        print(f"Cheapest flight from {ORIGIN_CITY_CODE}-{dest_city} with {cheapest_flight.stopovers} stops: INR {cheapest_flight.price}")
        if cheapest_flight.price < price_data["lowestPrice"]:
            print("Updating lowest price...")
            data_manager.update_lowest_price(price_data, cheapest_flight.price)
            notification.send_email(cheapest_flight, users_email_data)
        else:
            print("No update required.")