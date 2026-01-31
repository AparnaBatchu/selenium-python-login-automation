from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Launch browser
driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")  # demo testing site
driver.maximize_window()

# Login credentials
username = driver.find_element(By.ID, "user-name")
password = driver.find_element(By.ID, "password")

username.send_keys("standard_user")
password.send_keys("secret_sauce")
password.send_keys(Keys.RETURN)  # Press ENTER to login

time.sleep(3)  # Wait for page to load

# Verify login
if "inventory" in driver.current_url:
    print("Login successful")
else:
    print("Login failed")

driver.quit()  # Close browser
