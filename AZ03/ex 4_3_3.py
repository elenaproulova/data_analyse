import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Чтение данных из файла prices-cleaned.csv
data = pd.read_csv('prices_cleaned.csv')

# Предположим, что данные содержатся в столбце с названием 'price'
# Замените 'price' на название столбца, содержащего ваши числовые данные
prices = data['Price']

# Вычисление среднего значения
mean_value = np.mean(prices)

# Вывод среднего значения
print(f"Среднее значение: {mean_value}")

# Построение гистограммы
plt.hist(prices, bins=8, edgecolor='black')
plt.title('Гистограмма цен на диваны')
plt.xlabel('Значения')
plt.ylabel('Частота')
plt.axvline(mean_value, color='red', linestyle='dashed', linewidth=1, label='Среднее значение')
plt.legend()
plt.show()