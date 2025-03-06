from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)


driver.get("https://www.youtube.com")


WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, "search_query"))
)


search_box = driver.find_element(By.NAME, "search_query")
search_box.send_keys("Python tutorial" + Keys.RETURN)


WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "video-title"))
)


first_video = driver.find_element(By.ID, "video-title")
first_video.click()


WebDriverWait(driver, 30).until(
    EC.presence_of_element_located((By.CLASS_NAME, "video-stream"))
)


driver.quit()
