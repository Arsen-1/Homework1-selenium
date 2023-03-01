from selenium import webdriver
import time

def startBrowser(name):
    """
    browsers，"firefox"、"chrome"、"ie"、"phantomjs"
    """
    try:
        if name == "firefox" or name == "Firefox" or name == "ff":
            print("start browser name :Firefox")
            driver = webdriver.Firefox()
            driver.save_screenshot()
            return driver
        elif name == "chrome" or name == "Chrome":
            print("start browser name :Chrome")
            driver = webdriver.Chrome()
            return driver
        elif name == "Edge" or name == "edge":
            print("start browser name :Ie")
            driver = webdriver.Ie()
            return driver
        else:
            print("Not found this browser,You can use ‘firefox‘, ‘chrome‘, ‘ie‘")
    except Exception as msg:
        print("message: %s" % str(msg))

def run_case(name):
    driver = startBrowser(name)
    driver.get("https://www.demoblaze.com/")
    time.sleep(3)
    print(driver.title)
    driver.close()
    driver.quit()

if __name__ == "__main__":
    names = ["chrome", "firefox", "edge"]
    for i in names:
        run_case(i)

startBrowser('chrome')