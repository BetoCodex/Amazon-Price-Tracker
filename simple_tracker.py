from attr import attr
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from bs4 import BeautifulSoup
import re
import time

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
# Selecting a browser to work on
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://amazon.com")

driver.implicitly_wait(10)

delay = 8

# Setting Postal code
'''
driver.find_element(By.ID, "nav-global-location-popover-link").click()
postcode_field = driver.find_element(By.ID, "GLUXZipUpdateInput")
postcode_field.send_keys("33178")
driver.find_element(By.XPATH, "//*[@id='GLUXZipUpdate']/span/input").send_keys(Keys.RETURN)
try:
    element = WebDriverWait(driver, delay).until(
        EC.presence_of_element_located((By.ID, "a-autoid-1-announce"))
    )
    close_element = driver.find_element(By.ID, "a-autoid-1-announce").send_keys(Keys.RETURN)
except TimeoutException:
    print("Loading took to much time")
    '''

# Product Search Term
search_term = "guess sneakers"

# Targetting top searchbox
try:
    element = WebDriverWait(driver, delay).until(
        EC.presence_of_element_located((By.ID, 'twotabsearchtextbox'))
    )
    print("Page is ready")
    search_box = driver.find_element(By.ID, "twotabsearchtextbox")
    search_box.send_keys(search_term)
    search_box.send_keys(Keys.RETURN)
except TimeoutException:
    print("Loading took to much time")

# Getting Current URL to be use in BeautifulSoup
current_url = driver.current_url
driver.get(current_url)

# Filtering By Price
min_price = 15
max_price = 45

min_price_filter = driver.find_element(By.ID, "low-price").send_keys(min_price)
max_price_filter = driver.find_element(By.ID, "high-price").send_keys(max_price)
go_btn = driver.find_element(By.XPATH, '//*[@id="a-autoid-1"]/span/input').send_keys(Keys.RETURN)

# Getting Title and Subtitles for products
products_title_list = []
results = driver.find_elements(By.CLASS_NAME, "a-size-base-plus")
for result in results:
    products_title_list.append(result.text)

print(products_title_list)

# Getting Prices
products_price_list = []
result = driver.find_element(By.CLASS_NAME, "a-price-whole")
for result in results:
    products_price_list.append(result.text)

print(products_price_list)


time.sleep(6)



