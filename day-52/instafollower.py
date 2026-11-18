from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASE_URL = "https://app.100daysofpython.dev/services/share-a-naan"   # If using the mock
LOGIN_URL = f"{BASE_URL}/login"

class InstaFollower:
    def __init__(self, user, password):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)
        self.user = user
        self.password = password

    def login(self):
        print("In login")

    def find_followers(self):
        print("In find followers")

    def follow(self):
        print("In follow")