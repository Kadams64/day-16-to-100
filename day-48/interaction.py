from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True) # keep the browser open
driver = webdriver.Chrome(options=chrome_options)

# driver.get("https://en.wikipedia.org/wiki/Main_Page")
#
# total_number_element = driver.find_element(By.CSS_SELECTOR, value="div#articlecount")
# count = total_number_element.find_element(By.CSS_SELECTOR, value="span#mwDw")
# # count.click()
#
# search = driver.find_element(By.NAME, value="search")
# search.send_keys("Python")
# search.send_keys(Keys.ENTER)

driver.get("https://appbrewery.github.io/fake-newsletter-signup/")
f_name = driver.find_element(By.NAME, value="fName")
l_name = driver.find_element(By.NAME, value="lName")
email = driver.find_element(By.NAME, value="email")
f_name.send_keys("Kelly")
l_name.send_keys("Adams")
email.send_keys("kadams1@telus.net")
button = driver.find_element(By.XPATH,value='//*[@id="signup-form"]/button')
button.click()

#driver.quit()