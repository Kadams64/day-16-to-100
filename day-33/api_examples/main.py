import requests
from datetime import datetime, timedelta, timezone
import zoneinfo

def convert_utc_to_vancouver(time_str: str) -> str:
    # 1. Parse the AM/PM time string.
    # Python automatically assigns a default placeholder date of Jan 1, 1900.
    utc_dt = datetime.strptime(time_str, "%I:%M:%S %p")

    # 2. Make the datetime object aware that it is in UTC
    utc_dt = utc_dt.replace(tzinfo=zoneinfo.ZoneInfo("UTC"))

    utc_minus_7 = timezone(timedelta(hours=-7))
    # 3. Convert to the America/Vancouver timezone
    # America/Vancouver time is still set to UTC -8 instead of -7 as it should be
    # not sure why my pythons and macOS timezone files would be out of whack in that regard, but
    # they are
    vancouver_dt = utc_dt.astimezone(utc_minus_7)
    print(f"UTC Offset: {vancouver_dt.strftime('%z')}")

    # 4. Format the output back to an AM/PM time string
    return vancouver_dt.strftime("%I:%M:%S %p")

MY_LAT = 49.325699
MY_LONG = -117.665710

# response= requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status() # raise suitable HTTP Exceptions on error
#
# data = response.json()
# latitude = data["iss_position"]["latitude"]
# longitude = data["iss_position"]["longitude"]
#
# iss_position = (latitude, longitude)
#
# # https://latlong.net/Show-Latitude-Longitude.html
# print(iss_position)
# print(f"is type= {type(iss_position)}")

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
# The sunrise-sunset calculator is supposed to automatically determine time
# zone but it fails to do so.  It also ignores 'tz' values; all times are
# UTC.  So I hacked together a converter with help from Google AI
# docs are here=> https://sunrise-sunset.org/api

# even with the conversion it still seems to be off by an hour or so: not sure what
# the deal here is, whether I'm mistaken in my assessment that sunrise-sunset
# is at fault

#sunrise = convert_utc_to_vancouver(data["results"]["sunrise"])
#sunset = convert_utc_to_vancouver(data["results"]["sunset"])
sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]
print(f"Sunrise is= {sunrise}, sunset is={sunset}")
# print(f"raw API Sunrise is {data["results"]["sunrise"]}, sunset is {data["results"]["sunset"]}")
print(sunrise.split("T")[1].split(":"))
