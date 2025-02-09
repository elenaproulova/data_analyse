import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.devtools.v85.fetch import continue_request

driver = webdriver.Chrome()
url = "https://www.divan.ru/ekaterinburg/category/divany"
driver.get(url)
time.sleep(3)

svets = driver.find_elements(By.CSS_SELECTOR, 'div._Ud0k')

parsed_data = []

for svet in svets:
    try:
        price = svet.find_element(By.CSS_SELECTOR, 'div.pY3d2').text

    except:
        print("произошла ошибка при парсинге")
        continue

    parsed_data.append([price])
driver.quit()

with open("divan_price.csv", 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Цена'])
    writer.writerows(parsed_data)