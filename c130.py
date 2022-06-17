import pandas as pd
import csv

df = pd.read_csv('unit_converted_stars.csv')

df.drop(['Unnamed: 0'],axis=1,inplace=True)
print(df.columns)

cleaned_data = df.dropna()

cleaned_data.to_csv('cleaned_data.csv')
