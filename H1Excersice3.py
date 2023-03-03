from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException

def locate_categories_elements(element_name):
    driver = webdriver.Chrome()
    driver.get("https://www.demoblaze.com/")
    wait = WebDriverWait(driver, timeout=10)

    try:
        if element_name == "phones":
            phone_button = driver.find_element(By.CSS_SELECTOR, "div.list-group a:nth-of-type(2)")
            print("Element is located")
        elif element_name == "laptops":
            laptop_button = driver.find_element(By.CSS_SELECTOR, "div.list-group a:nth-of-type(3)")
            print("Element is located")
        elif element_name == "monitors":
            monitors_button = driver.find_element(By.CSS_SELECTOR, "div.list-group a:nth-of-type(4)")
            print("Element is located")
        else:
            raise NoSuchElementException
    except NoSuchElementException:
        print("No Such Element")


locate_categories_elements("laptops")
