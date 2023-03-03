from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException


def locate_header_elements(element_name):
    driver = webdriver.Chrome()
    driver.get("https://www.demoblaze.com/")
    wait = WebDriverWait(driver, timeout=10)

    try:
        if element_name == "home":
            home_button = driver.find_element(By.XPATH, "//*[@class = 'nav-link'][@href = 'index.html']")
            print("Element is located")
        elif element_name == "contact":
            contact_button = driver.find_element(By.XPATH, "//*[@data-target = '#exampleModal']")
            print("Element is located")
        elif element_name == "about us":
            about_us_button = driver.find_element(By.XPATH, "// *[@data-target = '#videoModal']")
            print("Element is located")
        elif element_name == "cart":
            cart_button = driver.find_element(By.XPATH, "//*[@id = 'cartur']")
            print("Element is located")
        elif element_name == "log in" or element_name.lower() == "login":
            login_button = driver.find_element(By.XPATH, "//*[@id = 'login2']")
            print("Element is located")
        elif element_name == "sign up":
            sign_up_button = driver.find_element(By.XPATH, "(//*[text()= 'Sign up'])[3]")
            print("Element is located")
        else:
            raise NoSuchElementException
    except NoSuchElementException:
        print("No Such Element")

locate_header_elements("sign up")
