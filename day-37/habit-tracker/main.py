import os
import requests
from dotenv import load_dotenv
from datetime import datetime

load_dotenv("/Users/kellyadams/PycharmProjects/day-16-to-100/.env")

PIXELA_ENDPOINT = "https://pixe.la/v1/users"
PIXELA_TOKEN = os.environ.get("PIXELA_TOKEN")
PIXELA_USERNAME = "kellyadams"
GRAPH_ID = "codingtime"

user_params = {
    "token": PIXELA_TOKEN,
    "username": PIXELA_USERNAME ,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# creates a new user
# response = requests.post(url=PIXELA_ENDPOINT,json=user_params)
# print(response.text)

graph_config = {
    "id" : GRAPH_ID,
    "name": "Coding Time",
    "unit": "Minutes",
    "type": "int",
    "color": "momiji",

}


graph_endpoint = f"{PIXELA_ENDPOINT}/{PIXELA_USERNAME}/graphs"

header_params = {
    "X-USER-TOKEN": PIXELA_TOKEN,
}

# creates a new graph
# response = requests.post(url=graph_endpoint, json=graph_config, headers=header_params)
# print(response.text)

# creates this graph=> https://pixe.la/v1/users/kellyadams/graphs/codingtime.html
# today = datetime.now()
today = datetime(year=2026, month=10, day=27)
pixel_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "240",

}

# create a dot on the graph
# response = requests.post(url=f"{graph_endpoint}/{GRAPH_ID}", json=pixel_config,
#                          headers=header_params)
# print(response.text)

# update a dot on the graph
pixel_update = {
    "quantity": "120",

}
# response = requests.put(url=f"{graph_endpoint}/{GRAPH_ID}/{today.strftime("%Y%m%d")}",
#                         json=pixel_update, headers=header_params)
# print(response.text)

# delete a dot on the graph
response = requests.delete(url=f"{graph_endpoint}/{GRAPH_ID}/{today.strftime("%Y%m%d")}",
                        headers=header_params)
print(response.text)