from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep,time
from selenium.common.exceptions import NoSuchElementException

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True) # keep the browser open
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://ozh.github.io/cookieclicker/")

"""<div class="langSelectButton title" style="padding:4px;" id="langSelect-EN">English</div>"""
# Get past language select
sleep(3)
lang_english = driver.find_element(By.ID, value="langSelect-EN")
lang_english.click()

sleep(2)
# cookie button

TIMEOUT_SECONDS = 240 * 60
# TIMEOUT_SECONDS = 30
start_time = time()
last_time = time()
counter = 0

while time() - start_time < TIMEOUT_SECONDS:
    cookie = driver.find_element(By.CSS_SELECTOR, value="button#bigCookie")
    cookie.click()
    counter += 1

    if time() - last_time > 10:
        print("check for upgrades")

        # stolen from solution code because I was stumped
        try:
            # Get current cookie count
            cookies_element = driver.find_element(by=By.ID, value="cookies")
            cookie_text = cookies_element.text
            # Extract number from text like "123 cookies"
            cookie_count = int(cookie_text.split()[0].replace(",", ""))

            # Find all available products in the store
            products = driver.find_elements(by=By.CSS_SELECTOR, value="div[id^='product']")

            # Find the most expensive item we can afford
            best_item = None
            for product in reversed(products):  # Start from most expensive (bottom of list)
                # Check if item is available and affordable (enabled class)
                if "enabled" in product.get_attribute("class"):
                    best_item = product
                    break

            # Buy the best item if found
            if best_item:
                best_item.click()
                print(f"Bought item: {best_item.get_attribute('id')}")

        except (NoSuchElementException, ValueError):
            print("Couldn't find cookie count or items")



        last_time = time()

cookies_element = driver.find_element(by=By.ID, value="cookies")
cookie_text = cookies_element.text
cookie_count = float(cookie_text.split()[0].replace(",", ""))
print(f"Final result: {cookies_element.text}")
print(f"Cookies/second: {cookie_count / TIMEOUT_SECONDS:.2f}")