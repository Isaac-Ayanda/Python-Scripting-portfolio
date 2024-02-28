from selenium import webdriver

def get_driver():
    # Set options to make browsing easier
    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobars")
    options.add_argument("start-maximized")
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("no-sandbox")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument("disable-blink-feature=AutomationControlled")

    driver = webdriver.Chrome(options=options)
    driver.get("http://automated.pythonanywhere.com/login/")
    return driver

def main():
    driver = get_driver()
    driver.find_element(by="id", value="id_username").send_keys("automated")
    driver.find_element(by="id", value="id_password").send_keys("automatedautomated")
    

print(main()) 