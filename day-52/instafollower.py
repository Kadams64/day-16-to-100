from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASE_URL = "https://app.100daysofpython.dev/services/share-a-naan"   # If using the mock
LOGIN_URL = f"{BASE_URL}/login"

SIMILAR_ACCOUNT = "chefsteps"   # the account whose followers you'll follow

class InstaFollower:
    def __init__(self, user, password):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)
        self.user = user
        self.password = password

    def login(self):
        self.driver.get(LOGIN_URL)
        username_input = (WebDriverWait(self.driver, 10)
            .until(EC.visibility_of_element_located((By.ID, 'username'))))
        password_input = self.driver.find_element(By.ID,"password")
        username_input.send_keys(self.user)
        password_input.send_keys(self.password)
        button = self.driver.find_element(By.CSS_SELECTOR,"button[type='submit'].naan-btn-primary")
        button.click()
        # the 'save your login info' popup can't be dismissed: just re-navigate to the
        # share-a-naan site
        time.sleep(2)
        self.driver.refresh()

    def find_followers(self):
        print("In find followers")
        # navigate to followers page
        self.driver.get(f"{BASE_URL}/u/{SIMILAR_ACCOUNT}/followers")
        time.sleep(2)
        scrollable = self.driver.find_element(By.CSS_SELECTOR, "div .followers-scroll")

        # works with infinite scrolling dialogues
        last_height = self.driver.execute_script("return arguments[0].scrollHeight", scrollable)
        while True:
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scrollable)
            time.sleep(1.5)  # Wait for new items to load

            new_height = self.driver.execute_script("return arguments[0].scrollHeight", scrollable)
            if new_height == last_height:
                break
            last_height = new_height

    def follow(self):
        print("In follow")
        all_buttons = self.driver.find_elements(By.CSS_SELECTOR, ".followers-scroll button")
        for button in all_buttons:
            try:
                button.click()
                time.sleep(1)
            except ElementClickInterceptedException:
                # An "Unfollow?" dialog opened (you already follow this account).
                cancel = self.driver.find_element(By.XPATH, "//button[contains(text(), 'Cancel')]")
                cancel.click()