import os

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True) # keep the browser open


TINDOG_URL = "https://app.100daysofpython.dev/services/tindog/u/K_NkijZzlCiY8_X0_o65BUuZQV3yUxKI"
FB_EMAIL = os.environ.get("FB_EMAIL")
FB_PASSWORD = os.environ.get("FB_PASSWORD")

driver = webdriver.Chrome(options=chrome_options)
driver.get(TINDOG_URL)
page_div = (WebDriverWait(driver, 10)
            .until(EC.presence_of_element_located((By.CLASS_NAME, "tindog-footer"))))
# created an account using Facebark on Tindog, used Udemy credentials
# Step 2: Navigate to the login page
"""<button type="button" class="btn-tindog-login tindog-login-pill" 
data-bs-toggle="modal" data-bs-target="#login-modal">Log in</button>"""
login_btn = driver.find_element(By.CLASS_NAME,"btn-tindog-login")
login_btn.click()

# note the EC (Expected condition) 'visibility_of_element' works properly here
# whereas presence_of_element fails with the button not being clickable
fb_btn = (WebDriverWait(driver, 10)
            .until(EC.visibility_of_element_located((By.CLASS_NAME, "btn-facebark"))))
fb_btn.click()

# Step 3: Login with Facebook

# switch to the new Facebark login window from the previous step
main_window = driver.window_handles[0]
facebark_window = driver.window_handles[1]
driver.switch_to.window(facebark_window)

email_input = (WebDriverWait(driver, 10)
            .until(EC.visibility_of_element_located((By.ID, "email"))))
password_input = driver.find_element(By.ID, "pass")
email_input.send_keys(FB_EMAIL)
password_input.send_keys(FB_PASSWORD)
login_btn = driver.find_element(By.XPATH,"/html/body/div[2]/div/form/button")
login_btn.click()
driver.switch_to.window(main_window)

# Step 4: dismiss all requests
allow_location = (WebDriverWait(driver, 10)
            .until(EC.visibility_of_element_located((By.XPATH, "/html/body/main/div/div/form/button"))))
allow_location.click()

notifications =  (WebDriverWait(driver, 10)
            .until(EC.visibility_of_element_located((By.XPATH, "/html/body/main/div/div/form/button[2]"))))
notifications.click()

cookies = (WebDriverWait(driver, 10)
            .until(EC.visibility_of_element_located((By.XPATH, "/html/body/main/div/div/form/button"))))
cookies.click()



# Step 5: hit like!
# following the guide we only get 20 likes per run of TinDog, so use them all up (excluding matches)
for _ in range(20):
    try:
        like_button = (WebDriverWait(driver, 10)
            .until(EC.presence_of_element_located((By.CLASS_NAME, "btn-like"))))

        # the like button was out of the viewport and couldn't be clicked reliably
        # this scrolls it into view
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", like_button)
        like_button.click()
        time.sleep(2)
    except ElementClickInterceptedException:
        match_link = (WebDriverWait(driver, 10)
                       .until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".match-popup a"))))
        match_link.click()
        time.sleep(1)
    except NoSuchElementException:
        time.sleep(2)
