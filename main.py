import pandas as pd

df = pd.read_csv('Dataset_spine.csv')

print(df.head())
print(df.info())
print(df.describe())
print(df['Class_att'])
print(df.loc[256])
print(df.loc[256,'pelvic tilt'])