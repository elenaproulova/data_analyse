import pandas as pd

# Чтение данных из файла prices.csv
data = pd.read_csv('prices.csv')

# Функция для очистки строки и преобразования в число
def clean_price(price_str):
    # Проверяем, является ли значение строкой
    if isinstance(price_str, str):
        # Удаляем "руб." и пробелы, затем преобразуем в число
        return int(price_str.replace('руб.', '').replace(' ', '').strip())
    else:
        # Если не строка, возвращаем NaN или 0
        return pd.NA  # или return 0

# Применяем функцию к столбцу 'Price'
data['Price'] = data['Price'].apply(clean_price)

# Записываем очищенные данные обратно в новый файл prices_cleaned.csv
data.to_csv('prices_cleaned.csv', index=False)

# Выводим сообщение о завершении
print("Данные успешно записаны в файл prices_cleaned.csv")
