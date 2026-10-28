import requests

api_key="APIKEY"
MY_LAT = 49.325699
MY_LONG = -117.665710
# https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API key}
# https://api.openweathermap.org/data/2.5/weather?lat=49.325699&lon=-117.665710&appid=138c1a66b98f63099b03af795c4ee419

# 5 day 3 hour forcast API call:
# api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={API key}
# api.openweathermap.org/data/2.5/forecast?lat=49.325699&lon=-117.665710&appid=138c1a66b98f63099b03af795c4ee419

# Weather condition codes:
# https://openweathermap.org/api/weather-conditions#Weather-Condition-Codes-2


parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": api_key,
    "cnt": 4,
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()
weather_data = response.json()

# for weather in weather_data["list"]:
#     weather_code = weather["weather"][0]["id"]
#     if weather_code < 700:
#         print("Bring an umbrella: its raining today!")
#         break
weather_codes = []
for weather in weather_data["list"]:
    weather_code = int(weather["weather"][0]["id"])
    weather_codes.append(weather_code)

threshold = 700
rain_in_forecast = bool([x for x in weather_codes if x < threshold])
if rain_in_forecast:
    print("Bring an umbrella: its raining today!")
