import requests
from twilio.rest import Client

ACCOUNT_SID = "<TWILIO_ACCOUNT_SID>"
AUTH_TOKEN = "<TWILIO_AUTH_TOKEN>"

API_KEY = "<OPEN_WEATHER_MAP_API_KEY>"
URL = "https://api.openweathermap.org/data/2.5/forecast"

params = {
    "lat": 22.250601,  #22.250601.    28.613939
    "lon": 68.980202,  #68.980202.    77.209023
    "appid": API_KEY,
    "units": "metric",
    "cnt": 4
}

response = requests.get(url=URL, params=params)
response.raise_for_status()
#print(response.json())
weather_forecast_data = response.json()
will_rain = False
for forecast in weather_forecast_data["list"]:
    weather_condition = forecast["weather"][0]["id"]
    if int(weather_condition) < 700 :
        will_rain = True

if will_rain:
    print("Today it gonna rain! Keep ur umbrella handy!")

    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    message = client.messages.create(
            body="sms_event_notifications", #free account. doesn't allow to send custom mssg
            from_="whatsapp:+17372508034",
            to="whatsapp:+918800975045",
            content_sid="HX8dc9eea84231541b091557c47cc2a342"
    )
    print(message.body)