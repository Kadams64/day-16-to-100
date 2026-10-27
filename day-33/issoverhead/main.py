import math
import time as t

import requests
from datetime import time, datetime, timedelta, timezone
import zoneinfo
import smtplib

MY_LAT = 49.325699
MY_LONG = -117.665710

VARIANCE = 5

MY_EMAIL = "someemail@gmail.com"
MY_PASSWORD = "somepass"

def email(msg_subject, msg_body, msg_to):
    # Google had no "App Passwords" option and I had to find and use the direct link
    # to get to it=> https://myaccount.google.com/apppasswords

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=msg_to,
                            msg=f"Subject:{msg_subject}\n\n{msg_body}")

def convert_utc_to_vancouver(time_str: str) -> str:
    """convert a iso8601 time string presumed to be in UTC time to
    the Vancouver timezone UTC -7.  No real error handling- beware!"""
    #assumes the parameter is an ISO date format string
    utc_dt = datetime.fromisoformat(time_str)

    # 2. Make the datetime object aware that it is in UTC
    utc_dt = utc_dt.replace(tzinfo=zoneinfo.ZoneInfo("UTC"))

    utc_minus_7 = timezone(timedelta(hours=-7))
    # 3. Convert to the America/Vancouver timezone
    # America/Vancouver time is still set to UTC -8 instead of -7 as it should be
    # not sure why my pythons and macOS timezone files would be out of whack in that regard, but
    # they are
    vancouver_dt = utc_dt.astimezone(utc_minus_7)

    # 4. Format the output back to an AM/PM time string
    return vancouver_dt.isoformat()

def is_time_in_range(start: time, end: time, current: time) -> bool:
    """Returns True if current time is within the start and end interval."""
    if start <= end:
        # Same-day range (e.g., 09:00 to 17:00)
        return start <= current <= end
    else:
        # Overnight range crossing midnight (e.g., 22:00 to 06:00)
        return start <= current or current <= end


def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    print(f"iss_latitude= {iss_latitude}; iss_longitude= {iss_longitude}")
    print(f"MY_LAT= {MY_LAT}; MY_LONG= {MY_LONG}")
    if (math.isclose(iss_latitude, MY_LAT, abs_tol=VARIANCE)
            and math.isclose(iss_longitude,MY_LONG, abs_tol=VARIANCE)):
        return True
    else:
        return False


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

email_sent = False

while True:

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()

    # the sunrise-sunset.org api doesn't properly reflect timezones; everything seems
    # to be in UTC despite the API documentation saying otherwise.  So I did some
    # timezone conversion
    sunrise_converted = convert_utc_to_vancouver(data["results"]["sunrise"])
    sunset_converted = convert_utc_to_vancouver(data["results"]["sunset"])
    sunrise = int(sunrise_converted.split("T")[1].split(":")[0])
    sunset = int(sunset_converted.split("T")[1].split(":")[0])

    time_now = int(datetime.now().hour)
    print(f"Sunrise hour= {sunrise}; sunset hour= {sunset}; time_now hour= {time_now}")
    sunset_time = time(sunset,0)
    sunrise_time = time(sunrise,0)
    now_time = time(time_now,0)

    if is_time_in_range(start=sunset_time, end= sunrise_time, current=now_time):
        print("It is dark enough")
        if is_iss_overhead() and not email_sent:
            email(msg_subject="The ISS is passing over!",
                  msg_body="Get outside and look up.  If the sky is clear you might see the space station.",
                  msg_to="kadams1@telus.net")
            email_sent = True # If I have the logic on this right, the email will be sent once
                              # per 'Iss overhead' event;
        else:
            print("sorry, no ISS overhead.")
            email_sent = False
    else:
        print("it is not yet dark enough.")

    #If the ISS is close to my current position
    # and it is currently dark
    # Then send me an email to tell me to look up.
    # BONUS: run the code every 60 seconds.
    t.sleep(60)


