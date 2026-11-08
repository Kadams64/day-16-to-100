from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True) # keep the browser open
driver = webdriver.Chrome(options=chrome_options)

# driver.get("https://www.amazon.ca/Instant-Electric-Pressure-Sterilizer-Stainless/dp/B00FLYWNYQ/ref=sr_1_4")
driver.get("https://python.org")


# # https://selenium.dev/documentation/webdriver/elements/locators
# price_dollar = driver.find_element(By.CLASS_NAME,"a-price-whole")
# price_cents = driver.find_element(By.CLASS_NAME,value="a-price-fraction")
# print(f"the price is ${price_dollar.text}.{price_cents.text}")

# search_bar = driver.find_element(By.NAME, value="q")
# print(search_bar.get_attribute("placeholder"))
# button = driver.find_element(By.ID, value="submit")
# print(button.size)
#
# documentation_link = driver.find_element(By.CSS_SELECTOR, value=".documentation-widget a")
# print(documentation_link.text)
#
# bug_link = driver.find_element(By.XPATH, value='//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
# print(bug_link.text)

upcoming_raw = driver.find_elements(By.CSS_SELECTOR, value="div.event-widget ul.menu li")
upcoming_dict ={}
id = 0
for item in upcoming_raw:
    date = item.find_element(By.CSS_SELECTOR,value="time").text
    event = item.find_element(By.CSS_SELECTOR,value="a").text
    upcoming_dict.update(
        {
            id: {"time": date, "name": event}
        }
    )
    id += 1

print(upcoming_dict)

# driver.close() # close the active tab
driver.quit() # close the whole browser
