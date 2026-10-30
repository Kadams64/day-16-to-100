import datetime
import os
from dotenv import load_dotenv
import requests
from datetime import datetime

load_dotenv("/Users/kellyadams/PycharmProjects/day-16-to-100/.env")

HUNDREDDAYS_API_KEY = os.environ.get("100_DAYS_APIKEY")
HUNDREDDAYS_APP_ID = os.environ.get("100_DAYS_APPID")
BASEURL = "https://app.100daysofpython.dev"
EXERCISE_URI = "/v1/nutrition/natural/exercise"
SHEETY_ENDPOINT = os.environ.get("SHEETY_ENDPOINT")
SHEETY_TOKEN = os.environ.get("SHEETY_TOKEN")

headers = {
    "x-app-id": HUNDREDDAYS_APP_ID,
    "x-app-key": HUNDREDDAYS_API_KEY
}


def add_row_with_sheety(exercise: str, dur: str, cals: str):
    global headers
    now = datetime.now()

    now_date = now.strftime("%d/%m/%Y")
    now_time = now.strftime("%H:%M:%S")

    sheety_request = {
        "workout": {
            "date": now_date,
            "time": now_time,
            "exercise": exercise.title(),
            "duration": dur,
            "calories": cals
        }
    }

    sheety_headers = {
        "Authorization": f"Bearer {SHEETY_TOKEN}"
    }

    response = requests.post(url=SHEETY_ENDPOINT,
                             json=sheety_request, headers=sheety_headers)
    print(response.text)

exercise_endpoint = f"{BASEURL}{EXERCISE_URI}"
exercise_request = {
    "query": input("What kind of exercise did you do? "),
}



response = requests.post(url=exercise_endpoint, json=exercise_request, headers=headers)
exercise_json = response.json()
exercise_single = exercise_json["exercises"][0]
exercise = exercise_single["name"]
duration = exercise_single["duration_min"]
calories = exercise_single["nf_calories"]
add_row_with_sheety(exercise=exercise, dur=duration,cals=calories)
