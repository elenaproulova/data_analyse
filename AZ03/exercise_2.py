import pandas as pd

df = pd.read_csv('../dz.csv')
print(df.head())
print(df.info())

df.dropna(inplace=True)
print(df.head())
group = df.groupby('City')['Salary'].mean()
print(group)
df.to_csv('output_dz.csv', index=False)