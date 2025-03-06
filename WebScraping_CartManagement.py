from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import csv


service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)


driver.get("https://www.demoblaze.com/")


WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "navbarExample"))
)


search_box = driver.find_element(By.ID, "searchBox")
search_box.send_keys("Samsung" + Keys.RETURN)


WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.CLASS_NAME, "card-title"))
)


results = driver.find_elements(By.CLASS_NAME, "card-title")
print("Arama sonuçları:")
for result in results:
    print(result.text)


with open('products.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["Product Name", "Price"])

    for result in results:
        product_name = result.text
        product_price = result.find_element(By.XPATH, "../../div[2]/h5").text
        writer.writerow([product_name, product_price])


first_product = driver.find_element(By.LINK_TEXT, "Samsung galaxy s6")
first_product.click()


WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "btn-success"))
)


add_to_cart_button = driver.find_element(By.CLASS_NAME, "btn-success")
add_to_cart_button.click()


WebDriverWait(driver, 10).until(
    EC.alert_is_present()
)


alert = driver.switch_to.alert
alert.accept()


cart_button = driver.find_element(By.ID, "cartur")
cart_button.click()


WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "success"))
)


cart_items = driver.find_elements(By.CLASS_NAME, "success")
print("Sepetteki ürünler:")
for item in cart_items:
    print(item.text)


remove_button = driver.find_element(By.CLASS_NAME, "btn-danger")
remove_button.click()


checkout_button = driver.find_element(By.CLASS_NAME, "btn-success")
checkout_button.click()


WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "name"))
)

name_field = driver.find_element(By.ID, "name")
name_field.send_keys("John Doe")

country_field = driver.find_element(By.ID, "country")
country_field.send_keys("USA")

city_field = driver.find_element(By.ID, "city")
city_field.send_keys("New York")

card_field = driver.find_element(By.ID, "card")
card_field.send_keys("1234 5678 9101 1121")

month_field = driver.find_element(By.ID, "month")
month_field.send_keys("12")

year_field = driver.find_element(By.ID, "year")
year_field.send_keys("2025")


purchase_button = driver.find_element(By.CLASS_NAME, "btn-primary")
purchase_button.click()


WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "lead"))
)


confirmation_message = driver.find_element(By.CLASS_NAME, "lead")
print(confirmation_message.text)


driver.quit()

