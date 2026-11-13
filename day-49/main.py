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

class_cards = driver.find_elements(By.CSS_SELECTOR, "div[id^='class-card-']")

booked_count = 0
waitlisted_count = 0
already_booked = 0
already_waitlisted = 0
detailed_list = []

for card in class_cards:
    # Get the day title from the parent day group
    day_group = card.find_element(By.XPATH, "./ancestor::div[contains(@id, 'day-group-')]")
    day_title = day_group.find_element(By.TAG_NAME, "h2").text

    # Check if this is a Tuesday
    if "Tue" in day_title:
        # Check if this is a 6pm class
        time_text = card.find_element(By.CSS_SELECTOR, "p[id^='class-time-']").text
        if "6:00 PM" in time_text:
            # Get the class name
            class_name = card.find_element(By.CSS_SELECTOR, "h3[id^='class-name-']").text

            # Find and click the book button
            button = card.find_element(By.CSS_SELECTOR, "button[id^='book-button-']")
            if button.text =="Booked":
                already_booked += 1
                print(f"✓ Already booked: {class_name} on {day_title}")
                detailed_list.append(f"[Existing booking] {class_name} on {day_title}")
            elif button.text == "Waitlisted":
                already_waitlisted += 1
                print(f"✓ Already waitlisted: {class_name} on {day_title}")
                detailed_list.append(f"[Existing booking] {class_name} on {day_title}")
            else:
                if button.text == "Join Waitlist":
                    button.click()
                    waitlisted_count += 1
                    print(f"✓ Joined waitlist for: {class_name} on {day_title}")
                    detailed_list.append(f"[New waitlist] {class_name} on {day_title}")
                else:
                    button.click()
                    booked_count += 1
                    print(f"✓ Booked: {class_name} on {day_title}")
                    detailed_list.append(f"[New booking] {class_name} on {day_title}")

    # Check if this is a Tuesday
    if "Thu" in day_title:
        # Check if this is a 6pm class
        time_text = card.find_element(By.CSS_SELECTOR, "p[id^='class-time-']").text
        if "6:00 PM" in time_text:
            # Get the class name
            class_name = card.find_element(By.CSS_SELECTOR, "h3[id^='class-name-']").text

            # Find and click the book button
            button = card.find_element(By.CSS_SELECTOR, "button[id^='book-button-']")
            if button.text =="Booked":
                already_booked += 1
                print(f"✓ Already booked: {class_name} on {day_title}")
                detailed_list.append(f"[Existing booking] {class_name} on {day_title}")
            elif button.text == "Waitlisted":
                already_waitlisted += 1
                print(f"✓ Already waitlisted: {class_name} on {day_title}")
                detailed_list.append(f"[Existing booking] {class_name} on {day_title}")
            else:
                if button.text == "Join Waitlist":
                    button.click()
                    waitlisted_count += 1
                    print(f"✓ Joined waitlist for: {class_name} on {day_title}")
                    detailed_list.append(f"[New waitlist] {class_name} on {day_title}")
                else:
                    button.click()
                    booked_count += 1
                    print(f"✓ Booked: {class_name} on {day_title}")
                    detailed_list.append(f"[New booking] {class_name} on {day_title}")

print("------- Summary ---------")
print(f"Classes booked: {booked_count}")
print(f"Waitlists joined: {waitlisted_count}")
sum_booked_waitlisted = already_booked + already_waitlisted
print(f"Already booked/waitlisted: {sum_booked_waitlisted}")
print(f"Total classes processed: {booked_count + waitlisted_count + sum_booked_waitlisted}")

print("------- Detailed list ---------")
for detail in detailed_list:
    print(f" • {detail}")
