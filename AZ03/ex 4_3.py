import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By



driver = webdriver.Chrome()
url = "https://www.divan.ru/ekaterinburg/category/divany"
driver.get(url)
time.sleep(3)

prices = driver.find_elements(By.CLASS_NAME, "ui-LD-ZU.KIkOH")


# Открытие CSV файла для записи
with open('prices.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Price'])  # Записываем заголовок столбца

    # Записываем цены в CSV файл
    for price in prices:
        writer.writerow([price.text])

# Закрытие драйвера
driver.quit()



