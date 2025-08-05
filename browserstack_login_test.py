from selenium import webdriver
from selenium.webdriver.common.by import By
import time

USERNAME = "your_browserstack_username"
ACCESS_KEY = "your_browserstack_access_key"

desired_cap = {
    'os': 'Windows',
    'os_version': '10',
    'browser': 'Chrome',
    'browser_version': 'latest',
    'name': 'Task 04 - Cross-Browser Test',
    'build': 'Task_04_Build'
}

driver = webdriver.Remote(
    command_executor=f'https://{USERNAME}:{ACCESS_KEY}@hub-cloud.browserstack.com/wd/hub',
    desired_capabilities=desired_cap
)

driver.get("https://www.saucedemo.com/")
time.sleep(2)

# Login test
driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()
time.sleep(3)

if "inventory" in driver.current_url:
    print("✅ Login Passed on Chrome (BrowserStack)")
else:
    print("❌ Login Failed")

driver.quit()

