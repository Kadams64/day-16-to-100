import requests
import os
from twilio.rest import Client

# Find your Account SID at twilio.com/console
# Provision API Keys at twilio.com/console/runtime/api-keys
# and set the environment variables. See http://twil.io/secure


auth_token = os.environ.get("TWILIO_AUTH_TOKEN")
account_sid = os.environ.get("TWILIO_SID")
open_weather_api_key=os.environ.get("OWM_API_KEY")

FROM_PHONE = os.environ.get("TWILIO_PHONE")
MY_PHONE = os.environ.get("MY_PHONE")
MY_LAT = 49.325699
MY_LONG = -117.665710

def rain_in_forecast() -> bool:
    # Weather condition codes:
    # https://openweathermap.org/api/weather-conditions#Weather-Condition-Codes-2

    parameters = {
        "lat": MY_LAT,
        "lon": MY_LONG,
        "appid": open_weather_api_key,
        "cnt": 4,
    }

    response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast",
                            params=parameters)
    response.raise_for_status()
    weather_data = response.json()

    weather_codes = []
    for weather in weather_data["list"]:
        weather_code = int(weather["weather"][0]["id"])
        weather_codes.append(weather_code)

    threshold = 700
    rain_forecast = bool([x for x in weather_codes if x < threshold])
    return rain_forecast

if rain_in_forecast():

    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="Bring an umbrella: it's raining today ☔️",
        from_= FROM_PHONE,
        to= MY_PHONE
    )