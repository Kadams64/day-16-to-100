import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from datetime import date,timedelta
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True) # keep the browser open
user_data_dir = os.path.join(os.getcwd(), "chrome_profile")
chrome_options.add_argument(f"--user-data-dir={user_data_dir}")

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://appbrewery.github.io/gym/")
wait = WebDriverWait(driver, 2)

GYM_URL = "https://appbrewery.github.io/gym/"
ACCOUNT_EMAIL = os.environ.get("GYM_EMAIL")
ACCOUNT_PASSWORD = os.environ.get("GYM_PASSWORD")

def book_by_title(title: str):
    global already_booked, already_waitlisted, waitlisted_count, booked_count
    if title in day_title:
        # Check if this is a 6pm class
        time_text = card.find_element(By.CSS_SELECTOR, "p[id^='class-time-']").text
        if "6:00 PM" in time_text:
            # Get the class name
            class_name = card.find_element(By.CSS_SELECTOR, "h3[id^='class-name-']").text

            # Find and click the book button
            button = card.find_element(By.CSS_SELECTOR, "button[id^='book-button-']")
            if button.text == "Booked":
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
                    # button.click()
                    retry(lambda: book_class(button), description="Booking")
                    booked_count += 1
                    print(f"✓ Booked: {class_name} on {day_title}")
                    detailed_list.append(f"[New booking] {class_name} on {day_title}")

def verify_bookings():
    global already_booked, already_waitlisted, waitlisted_count, booked_count
    total_booked = already_booked + already_waitlisted + booked_count + waitlisted_count
    # navigate to My Bookings
    bookings_link = driver.find_element(By.ID,"my-bookings-link")
    bookings_link.click()

    # wait for page div to render
    page_div = (WebDriverWait(driver, 10)
         .until(EC.presence_of_element_located((By.ID, "my-bookings-page"))))

    verified_count = 0
    all_cards = driver.find_elements(By.CSS_SELECTOR, "div[id*='card-']")

    for card in all_cards:
        try:
            when_paragraph = card.find_element(By.XPATH, ".//p[strong[text()='When:']]")
            when_text = when_paragraph.text

            # Check if it's a Tuesday or Thursday 6pm class
            if ("Tue" in when_text or "Thu" in when_text) and "6:00 PM" in when_text:
                class_name = card.find_element(By.TAG_NAME, "h3").text
                print(f"  ✓ Verified: {class_name}")
                verified_count += 1
        except NoSuchElementException:
            # Skip if no "When:" text found (not a booking card)
            pass

    # Simple comparison
    print(f"\n--- VERIFICATION RESULT ---")
    print(f"Expected: {total_booked} bookings")
    print(f"Found: {verified_count} bookings")

    if total_booked == verified_count:
        print("✅ SUCCESS: All bookings verified!")
    else:
        print(f"❌ MISMATCH: Missing {total_booked - verified_count} bookings")

def login():
    login = driver.find_element(By.ID, "login-button")
    login.click()
    email = (WebDriverWait(driver, 10)
             .until(EC.presence_of_element_located((By.ID, "email-input"))))
    # email = driver.find_element(By.ID, "email-input")

    email.clear()
    email.send_keys(ACCOUNT_EMAIL)

    password = driver.find_element(By.ID, "password-input")
    password.clear()
    password.send_keys(ACCOUNT_PASSWORD)

    login_btn = driver.find_element(By.ID, "submit-button")
    login_btn.click()

    page_div = (WebDriverWait(driver, 10)
                .until(EC.presence_of_element_located((By.ID, "schedule-page"))))
    # I would have to try and catch a selenium.common.exceptions.TimeoutException here if I wanted
    # to test for success / failure

def retry(func, retries=7, description=None):
    for i in range(retries):
        print(f"Trying {description}. Attempt: {i + 1}")
        try:
            return func()
        except TimeoutException:
            if i == retries - 1:
                raise
            time.sleep(1)

def book_class(booking_button):
    booking_button.click()
    # Wait for button state to change - will time out if booking failed
    wait.until(lambda d: booking_button.text == "Booked")




retry(login, description="login")


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
    book_by_title("Tue")

    # Check if this is a Thursday
    book_by_title("Thu")

# print("------- Summary ---------")
# print(f"Classes booked: {booked_count}")
# print(f"Waitlists joined: {waitlisted_count}")
# sum_booked_waitlisted = already_booked + already_waitlisted
# print(f"Already booked/waitlisted: {sum_booked_waitlisted}")
# print(f"Total classes processed: {booked_count + waitlisted_count + sum_booked_waitlisted}")
#
# print("------- Detailed list ---------")
# for detail in detailed_list:
#     print(f" • {detail}")
verify_bookings()