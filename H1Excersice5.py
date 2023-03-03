from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as condition
import time

def loaded_correctly(button):

    driver = webdriver.Chrome()
    driver.get("https://demoblaze.com")
    wait = WebDriverWait(driver, timeout=10)
    wait.until(condition.all_of(condition.element_to_be_clickable((By.CSS_SELECTOR, "a#itemc")),
                                condition.visibility_of_element_located(
                                    (By.CSS_SELECTOR, "div#tbodyid div:nth-of-type(9)"))))
    if button == "phones":
        phones = driver.find_element(By.CSS_SELECTOR, "div.list-group a:nth-of-type(2)")
        assert not phones.is_selected()
        phones.click()
        wait.until(condition.visibility_of_element_located((By.XPATH, "//a[text()='HTC One M9']")))
        actual_amount = len(driver.find_elements(By.CSS_SELECTOR, "div.col-lg-4.col-md-6.mb-4"))
        expected_amount = 7
        assert actual_amount == expected_amount
    elif button == "laptops":
        laptops = driver.find_element(By.CSS_SELECTOR, "div.list-group a:nth-of-type(3)")
        assert not laptops.is_selected()
        laptops.click()
        wait.until(condition.visibility_of_element_located((By.XPATH, "//a[text()='Dell i7 8gb']")))
        first_page_actual_amount = len(driver.find_elements(By.CSS_SELECTOR, "div.col-lg-4.col-md-6.mb-4"))
        first_page_expected_amount = 6
        button_next = driver.find_element(By.CSS_SELECTOR, "button#next2")
        button_next.click()
        wait.until(condition.visibility_of_element_located((By.XPATH, "//a[text()='ASUS Full HD']")))
        second_page_actual_amount = len(driver.find_elements(By.CSS_SELECTOR, "div.col-lg-4.col-md-6.mb-4"))
        second_page_expected_amount = 6
        assert first_page_actual_amount == first_page_expected_amount
        assert second_page_actual_amount == second_page_expected_amount
    elif button == "monitors":
        monitor = driver.find_element(By.CSS_SELECTOR, "div.list-group a:nth-of-type(4)")
        assert not monitor.is_selected()
        monitor.click()
        wait.until(condition.visibility_of_element_located((By.XPATH, "//a[text()='Apple monitor 24']")))
        actual_amount = len(driver.find_elements(By.CSS_SELECTOR, "div.col-lg-4.col-md-6.mb-4"))
        expected_amount = 2
        assert actual_amount == expected_amount
        wait = WebDriverWait(driver, timeout=10)
    else:
        raise NoSuchElementException("There isn't button like that")

loaded_correctly("monitors")
#loaded_correctly("monitoraa")