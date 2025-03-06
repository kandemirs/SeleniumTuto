from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)


driver.get("https://www.seleniumeasy.com/test/basic-select-dropdown-demo.html")


WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "select-demo"))
)

dropdown = driver.find_element(By.ID, "select-demo")


select = Select(dropdown)
select.select_by_visible_text("Tuesday")


selected_option = driver.find_element(By.class_name, "selected-value")
print(selected_option.text)


driver.quit()
