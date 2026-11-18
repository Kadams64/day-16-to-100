import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv, find_dotenv

# Load environment variables from .env file
load_dotenv(find_dotenv())

ZILLOW_URL = "https://appbrewery.github.io/Zillow-Clone/"


def get_properties():
    response = requests.get(ZILLOW_URL)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")
    address_elements = soup.select('address[data-test="property-card-addr"]')
    price_elements = soup.select('span[data-test="property-card-price"]')
    url_elements = soup.select('a[data-test="property-card-link"].StyledPropertyCardDataArea-anchor')
    addresses = [clean_address(element.text) for element in address_elements]
    prices = [clean_prices(element.text) for element in price_elements]
    urls = [element.get("href") for element in url_elements]
    return addresses, prices, urls

def clean_address(string: str):
    cleaned = string.strip()
    cleaned = cleaned.replace("|", ",")
    return cleaned

def clean_prices(string: str):
    cleaned = string.split("+",1)[0]
    cleaned = cleaned.split("/",1)[0]
    return cleaned


def fill_forms(properties):
    # https://forms.gle/WiqrpvXoe6HQUJBC9
    addresses = properties[0]
    prices = properties[1]
    urls = properties[2]
    # print(f"address= {addresses[0]}\nprice= {prices[0]}\nurl= {urls[0]}")
    print(addresses)
    print(prices)
    print(urls)
    pass

rentals = get_properties()
fill_forms(rentals)