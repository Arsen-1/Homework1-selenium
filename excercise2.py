from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
service = Service(executable_path="/usr/local/bin/chromedriver")

#home   //*[@id="navbarExample"]/ul/li[1]/a
#contact  //*[@id="navbarExample"]/ul/li[2]/a
#about us   //*[@id="navbarExample"]/ul/li[3]/a
#cart //*[@id="cartur"]
#log in //*[@id="login2"]
#sign up //*[@id="signin2"]
try:
    service = Service(executable_path="/usr/local/bin/chromedriver")
    with webdriver.Chrome(service=service) as driver:
        driver.get('https://www.demoblaze.com/')
        # find element by xpath
        myDiv1 = driver.find_element(By.XPATH, '//*[@id="navbarExample"]/ul/li[1]/a')
        myDiv2 = driver.find_element(By.XPATH, '//*[@id="navbarExample"]/ul/li[2]/a')
        myDiv3 = driver.find_element(By.XPATH, '//*[@id="navbarExample"]/ul/li[3]/a')
        myDiv4 = driver.find_element(By.XPATH, '//*[@id="cartur"]')
        myDiv5 = driver.find_element(By.XPATH, '//*[@id="login2"]')
        myDiv6 = driver.find_element(By.XPATH, '//*[@id="signin2"]')
        print(myDiv1.text, myDiv2.text, myDiv3.text, myDiv4.text, myDiv5.text, myDiv6.text)
except Exception as msg:
    print("message: There is no such element")


    def test