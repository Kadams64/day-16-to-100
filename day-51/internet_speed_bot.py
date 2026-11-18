from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

SPEEDTEST_URL = "https://www.speedtest.net/"
Y_LOGIN_URL = "https://app.100daysofpython.dev/services/y/login"
PROMISED_DOWN = 1000
PROMISED_UP = 1000

class InternetSpeedTwitterBot:
    def __init__(self, email, password):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)
        self.up = 0
        self.down = 0
        self.email = email
        self.password = password


    def get_internet_speed(self):
        print("In get internet speed")
        self.driver.get(SPEEDTEST_URL)
        button = (WebDriverWait(self.driver, 10)
            .until(
            EC.visibility_of_element_located((
                By.XPATH, '//*[@id="root"]/div/div[1]/div/div[2]/div[2]/div[2]/div/div/div[2]/div[2]/button'))))
        button.click()
        time.sleep(60)

        # the upe and down load speed elements are not named like they are in the solution code.  The
        # XPATH only works about 30% of the time, and changes on some runs
        try:

            up_element = (WebDriverWait(self.driver, 10)
                .until(
                EC.visibility_of_element_located((
                    By.XPATH, '//*[@id="root"]/div/div[1]/div/div[2]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[2]/div[1]/div[2]/div/h3'))))
        except TimeoutException:
            print("timeout in up element; trying alternate XPATH")
            up_element = (WebDriverWait(self.driver, 10)
            .until(
                EC.visibility_of_element_located((
                    By.XPATH,
                    '//*[@id="root"]/div/div[1]/div/div[2]/div[2]/div[2]/div/div/div[1]/div[2]/div[2]/div[1]/div[2]/h3'))))
        try:
            down_element = (self.driver.
                            find_element(By.XPATH,
                                         '//*[@id="root"]/div/div[1]/div/div[2]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[2]/div[1]/div[1]/div/h3'))
        except TimeoutException:
            print("timeout in down element; trying alternate XPATH")
            down_element = (self.driver.
                            find_element(By.XPATH,
                                         '//*[@id="root"]/div/div[1]/div/div[2]/div[2]/div[2]/div/div/div[1]/div[2]/div[2]/div[1]/div[1]/h3'))

        self.up = float(up_element.text)
        self.down = float(down_element.text)

    def tweet_at_provider(self):
        print("in tweet_at_provider")
        if self.up < PROMISED_UP or self.down < PROMISED_DOWN:
            # navigate to Y site
            self.driver.get(Y_LOGIN_URL)
            email_input = (WebDriverWait(self.driver, 10)
                .until(EC.visibility_of_element_located((By.ID, 'email'))))
            password_input = self.driver.find_element(By.ID, "password")
            email_input.send_keys(self.email)
            password_input.send_keys(self.password)
            login_btn = self.driver.find_element(By.XPATH, "/html/body/div/div/form/button")
            login_btn.click()

            twit_content = (WebDriverWait(self.driver, 10)
                .until(EC.presence_of_element_located((By.ID, 'tweet-compose'))))
            # time.sleep(5)

            twit_content.send_keys(f"I was promised speeds of {PROMISED_UP} up/{PROMISED_DOWN} dn and "
                                   f"am getting {self.up}/{self.down}.  What gives?!")
            twit_post_btn = self.driver.find_element(By.ID, "post-btn")
            twit_post_btn.click()
        else:
            print("the provider is delivering promised speeds.  Don't tweet.")