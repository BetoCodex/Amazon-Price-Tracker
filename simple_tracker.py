from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
# Selecting a browser to work on
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://amazon.com")

driver.implicitly_wait(10)

delay = 8

# Postal Code
postal_code = "33178"

 # Product Search Term
search_term = "guess sneakers"

class AmazonAPI:
    def __init__(self):
        pass

    def run(self):
        print('Staring Script...')
        print(f"Looking for {search_term} products")
        self.setting_postal_code()
        print(f"Using postal code: {postal_code}")
        self.prodcut_search()
        self.price_filter()
        self.title_filter()


    def setting_postal_code(self):
        # Setting Postal code
        driver.find_element(By.ID, "nav-global-location-popover-link").click()
        postcode_field = driver.find_element(By.ID, "GLUXZipUpdateInput")
        postcode_field.send_keys(postal_code)
        driver.find_element(By.XPATH, "//*[@id='GLUXZipUpdate']/span/input").send_keys(Keys.RETURN)
        try:
            element = WebDriverWait(driver, delay).until(
                EC.presence_of_element_located((By.ID, "a-autoid-1-announce"))
            )
            close_element = driver.find_element(By.ID, "a-autoid-1-announce").send_keys(Keys.RETURN)
        except TimeoutException:
            print("Loading took to much time")
            
    
    def prodcut_search(self):
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
    # current_url = driver.current_url
    # driver.get(current_url)

    def price_filter(self):
        driver.implicitly_wait(3)
        # Filtering By Price
        min_price = 15
        max_price = 45
        # Targetting filtering box and applying min and max prices
        driver.find_element(By.ID, "low-price").send_keys(min_price)
        driver.find_element(By.ID, "high-price").send_keys(max_price)
        driver.find_element(By.XPATH, '//*[@id="a-autoid-1"]/span/input').send_keys(Keys.RETURN)

        # Storing prices in a list
        products_price_list = []
        results = driver.find_elements(By.CLASS_NAME, "a-price-whole")
        for result in results:
            products_price_list.append(result.text)
        
        print(products_price_list)

    def title_filter(self):
        # Getting Title and Subtitles for products
        products_title_list = []
        results = driver.find_elements(By.CLASS_NAME, "a-size-base-plus")
        for result in results:
            products_title_list.append(result.text)

        print(products_title_list)

    def getting_products_links(self):
        pass

if __name__ == '__main__':
    print('Hey!!')
    amazon = AmazonAPI()
    amazon.run()
    



