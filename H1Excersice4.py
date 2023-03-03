from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as condition
import time

def highest_price():
    driver = webdriver.Chrome()
    driver.get("https://demoblaze.com")
    wait = WebDriverWait(driver, timeout=10)
    wait.until(condition.visibility_of_all_elements_located(
        (By.CSS_SELECTOR, "div[class='col-lg-4 col-md-6 mb-4']")))
    product_quantity = driver.find_elements(By.CSS_SELECTOR, "div.col-lg-4.col-md-6.mb-4")
    prices = []
    n = 1
    for price in range(len(product_quantity)):
        prices.append(driver.find_element(By.CSS_SELECTOR, f"div#tbodyid div:nth-of-type({n}) h5").text)
        n += 1
    max_price = max(prices)
    max_price_product = driver.find_element(
        By.XPATH, f"//div[@class = 'card-block']/h5[text()='{max_price}']")
    product_name = driver.find_element(locate_with(By.TAG_NAME, "a").above(max_price_product)).text
    print(f"The highest price item in first page is {product_name}, which costs {max_price}.")

highest_price()
