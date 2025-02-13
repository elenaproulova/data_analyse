import pandas as pd

data = {
    'name' : ['Иван','Анна', 'Владимир', 'Виктор', 'Алена', 'Ирина', 'Тамара', 'Василий', 'Антон', 'Сергей'],
    'math' : [5, 4, 4, 3, 5, 2, 4, 3, 2, 1],
    'bio' : [3, 4, 1, 2, 5, 5, 3, 4, 5, 4],
    'rus' : [2, 3, 4, 4, 4, 5, 3, 2, 1, 5],
    'sport' : [5, 5, 5, 4, 4, 3, 3, 4, 5, 5],
    'hist' : [3, 3, 4, 4, 2, 1, 5, 4, 3, 2]
}

df = pd.DataFrame(data)

print(df.head())
print(df.describe())
print(f"Средняя оценка по математике - {df['math'].mean()}")
print(f"Средняя оценка по биологии - {df['bio'].mean()}")
print(f"Средняя оценка по русскому языку - {df['rus'].mean()}")
print(f"Средняя оценка по физкультуре - {df['sport'].mean()}")
print(f"Средняя оценка по истории - {df['hist'].mean()}")

print(f"Медианная оценка по математике - {df['math'].median()}")
print(f"Медианная оценка по биологии - {df['bio'].median()}")
print(f"Медианная оценка по русскому языку - {df['rus'].median()}")
print(f"Медианная оценка по физкультуре - {df['sport'].median()}")
print(f"Медианная оценка по истории - {df['hist'].median()}")

Q1_math = df['math'].quantile(0.25)
Q3_math = df['math'].quantile(0.75)

print(f"Квантиль Q1 (математика)  - {Q1_math}")
print(f"Квантиль Q3 (математика) - {Q3_math}")

print(f"Стандартное отклонение оценок по математике - {df['math'].std()}")
print(f"Стандартное отклонение оценок по биологии - {df['bio'].std()}")
print(f"Стандартное отклонение оценок по русскому языку - {df['rus'].std()}")
print(f"Стандартное отклонение оценок по физкультуре - {df['sport'].std()}")
print(f"Стандартное отклонение оценок по истории - {df['hist'].std()}")
