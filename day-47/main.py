import os
import smtplib
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv, find_dotenv

# Load environment variables from .env file
load_dotenv(find_dotenv())

# SALE_URL = "https://appbrewery.github.io/instant_pot/"
SALE_URL = "https://www.amazon.ca/Instant-Electric-Pressure-Sterilizer-Stainless/dp/B00FLYWNYQ/ref=sr_1_4"

TARGET_PRICE = 100.00

SENDER_EMAIL =  os.environ.get("MY_EMAIL")
SENDER_APP_PASSWORD = os.environ.get("MY_EMAIL_PASSWORD")

def send_email(msg_to, msg_subject, msg_body):
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=SENDER_EMAIL, password=SENDER_APP_PASSWORD)
        connection.sendmail(from_addr=SENDER_EMAIL, to_addrs=msg_to,
                            msg=f"Subject:{msg_subject}\n\n{msg_body}".encode("utf-8"))

header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/156.0.0.0 Safari/537.36",
    "Accept-Language": "en-US"
}
response = requests.get(SALE_URL, headers=header)
response.raise_for_status()


soup = BeautifulSoup(response.text, "html.parser")

'''<span class="a-price-whole">99<span class="a-price-decimal">.</span></span>
<span class="a-price-fraction">99</span>'''
float_whole = float(soup.select_one("span .a-price-whole").get_text())
float_fraction = float(soup.select_one("span .a-price-fraction").get_text())/100
float_price = float_whole + float_fraction

item_title = soup.select_one("span#productTitle").get_text()
item_title = " ".join(item_title.split()) # remove excess whitespace

if float_price < TARGET_PRICE:
    send_email(
        msg_to="kadams1@telus.net",
        msg_subject="Amazon Price Alert!",
        msg_body=f"{item_title} is now ${float_price}.\n{SALE_URL}")
else:
    print(f"Price for {item_title}\nis at ${float_price}\nabove target of ${TARGET_PRICE}")

