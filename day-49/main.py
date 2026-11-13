import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep,time
from datetime import date,timedelta
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

GYM_URL = "https://appbrewery.github.io/gym/"
ACCOUNT_EMAIL = os.environ.get("GYM_EMAIL")
ACCOUNT_PASSWORD = os.environ.get("GYM_PASSWORD")

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True) # keep the browser open
user_data_dir = os.path.join(os.getcwd(), "chrome_profile")
chrome_options.add_argument(f"--user-data-dir={user_data_dir}")

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://appbrewery.github.io/gym/")

login = driver.find_element(By.ID, "login-button")
login.click()
email = (WebDriverWait(driver, 10)
         .until(EC.presence_of_element_located((By.ID, "email-input"))))
# email = driver.find_element(By.ID, "email-input")
password = driver.find_element(By.ID, "password-input")
login_btn = driver.find_element(By.ID, "submit-button")
email.send_keys(ACCOUNT_EMAIL)
password.send_keys(ACCOUNT_PASSWORD)
login_btn.click()

page_div = (WebDriverWait(driver, 10)
         .until(EC.presence_of_element_located((By.ID, "schedule-page"))))
# I would have to try and catch a selenium.common.exceptions.TimeoutException here if I wanted
# to test for success / failure

today = date.today()
# Tuesday is weekday 1 (Monday=0, Tuesday=1, ..., Sunday=6)
days_ahead = (1 - today.weekday() + 7) % 7

# If today is already Tuesday, move to next week's Tuesday
if days_ahead == 0:
    days_ahead = 7

next_tuesday = today + timedelta(days=days_ahead)
next_tues_str = next_tuesday.strftime("%Y-%m-%d-1800")

book_btn = driver.find_element(By.CSS_SELECTOR, f"button[id$='{next_tues_str}']")
book_btn.click()
print(f"✅Booked class on {next_tues_str}")
