import os
import requests
from dotenv import load_dotenv
from datetime import date, timedelta
from twilio.rest import Client


# Pycharm seems to be having problems reading/processing .env files
# so I'm using the python-dotenv library

#directory name seems to only work if absolute to root or local to execution
load_dotenv("/Users/kellyadams/PycharmProjects/day-16-to-100/.env")
STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
STOCK_API_KEY = os.environ.get("ALPHA_VANTAGE_KEY")
NEWS_ENDPOINT = "https://eventregistry.org/api/v1/article/getArticles"
# the originally recommended URL throws an unauthorized (401) error
#NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_API_KEY = os.environ.get("NEWS_API_KEY")
TWILIO_AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")
TWILIO_SID = os.environ.get("TWILIO_SID")
FROM_PHONE = os.environ.get("TWILIO_PHONE")
MY_PHONE = os.environ.get("MY_PHONE")


def daily_stock_diff() -> float:

    parameters = {
        "function": "TIME_SERIES_DAILY",
        "symbol": STOCK_NAME,
        "outputsize": "compact",
        "apikey": STOCK_API_KEY,
    }

    response = requests.get(url=STOCK_ENDPOINT,
                            params=parameters)
    response.raise_for_status()
    json = response.json()
    daily_series = json["Time Series (Daily)"]

    # list comprehension to extract the two most recent entries in the time series
    # using the slice operator; I kept the dates
    recent_two_dicts = [{"date": date, **metrics} for date,
        metrics in list(daily_series.items())[:2]]
    yesterdays_closing = float(recent_two_dicts[0]["4. close"])
    day_befores_closing = float(recent_two_dicts[1]["4. close"])

    absolute_diff = abs(yesterdays_closing - day_befores_closing)
    percentage_change = (absolute_diff / day_befores_closing) * 100
    return percentage_change

def get_news(company: str) -> list[dict[str, Any]]:
    yesterday = date.today() - timedelta(days=1)
    yesterday_string = yesterday.strftime("%Y-%m-%d")
    parameters = {
        "dateStart": yesterday_string,
        "keyword": company,
        "articlesCount": 5,
        "resultType": "articles",
        "apiKey": NEWS_API_KEY,
    }

    response = requests.post(url=NEWS_ENDPOINT,
                            json=parameters)
    response.raise_for_status()

    return response.json()["articles"]["results"]

def send_to_twilio(stock_name, percentage_diff, item):
    headline = f"Headline: {item["headline"]}"
    brief = f"Brief: {item["body"]}"

    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
    message = client.messages.create(
        body=f"{stock_name} : {percentage_diff:.2f}\n{headline}\n{brief}",
        from_= FROM_PHONE,
        to= MY_PHONE
    )

stock_diff = daily_stock_diff()
print(f"stock_diff= {stock_diff}")
if stock_diff > 5:
    news_items = get_news(COMPANY_NAME)

    # slice to reduce the list to three items
    # arguably I could render this unnecessary by changing the query in
    # get_news
    three_articles = news_items[:3]


    # there is no article description in the returned data, so I'm concatenating the body
    # Template from Angela:
    # [new_item for item in list]
    new_list = [
        {
            "headline": item["title"],
            "body": item["body"][:140] + "..." if len(item["body"]) > 200 else item["body"]
         }
        for item in three_articles
    ]

    for news_item in new_list:
        send_to_twilio(STOCK_NAME, stock_diff, news_item)


#Optional  Format the message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

