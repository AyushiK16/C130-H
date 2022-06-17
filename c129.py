import pandas as pd
import csv

df = pd.read_csv("dwarf_stars.csv")
df = df.dropna()
df["Radius"] = 0.102763*df["Radius"]
df['Mass']=df['Mass'].apply(lambda x: x.replace('$', '').replace(',', '')).astype('float')

df.head()
df.drop(['Unnamed: 0'],axis=1,inplace=True)
df.reset_index(drop=True,inplace=True)
df.to_csv("unit_converted_stars.csv")

