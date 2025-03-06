from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time


service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)


driver.get("https://www.google.com")


time.sleep(2)


driver.save_screenshot("google_screenshot.png")
print("The screenshot has been taken and saved.")


driver.quit()
