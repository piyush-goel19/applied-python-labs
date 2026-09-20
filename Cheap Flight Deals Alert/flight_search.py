import os
import requests
from dotenv import load_dotenv

load_dotenv()

SERPAPI_URL = "https://serpapi.com/search"

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.api_key = os.getenv("SERPAPI_KEY")

    def check_flights(self, origin_city_code, destination_city_code, from_date, to_date, is_direct=True):
        params = {
            "engine": "google_flights",
            "departure_id": origin_city_code,
            "arrival_id": destination_city_code,
            "outbound_date": from_date,
            "return_date": to_date,
            "type": "1",
            "adults": 1,
            "currency": "INR",
            "sort_by": "2",
            "api_key": self.api_key,
            "stops": 1 if is_direct else 3,
        }

        response = requests.get(url=SERPAPI_URL, params=params)
        if response.status_code != 200:
            print(f"check flights response code: {response.status_code}")
            return None

        data = response.json()
        if "error" in data:
            print(f"check flights error: {data['error']}")
            return None
        return data