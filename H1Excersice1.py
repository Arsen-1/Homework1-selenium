from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import time


def browser(browser_name):
        if browser_name == "chrome":
            driver = webdriver.Chrome()
            driver.get("https://www.demoblaze.com/")
            wait = WebDriverWait(driver, timeout=10)
        elif browser_name == "firefox":
            driver = webdriver.Firefox()
            driver.get("https://www.demoblaze.com/")
            wait = WebDriverWait(driver, timeout=10)
        elif browser_name == "edge":
            driver = webdriver.Edge()
            driver.get("https://www.demoblaze.com/")
            wait = WebDriverWait(driver, timeout=10)
        else:
            print(f"'{browser_name}' is wrong")

browser("chrome")
browser("firefox")
browser("edge")
