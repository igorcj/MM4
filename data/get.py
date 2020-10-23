#!/usr/bin/env python3

import os
import wget
import pandas as pd

url = 'https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.csv'
filename = wget.download(url)

df = pd.read_csv(filename)

os.remove(filename)

print("\n" + filename)

df = df[df["location"] == "Canada"]
df = df[["date", "new_cases", "new_deaths"]]
df["date"] = pd.to_datetime(df["date"])
cases=[0,0,0,0,0,0,0]
deaths=[0,0,0,0,0,0,0]

for index, row in df.tail(len(df)-7).iterrows():
    cases.append(sum(df.loc[(index-7):(index-1),'new_cases'])/7)
    deaths.append(sum(df.loc[(index-7):(index-1),'new_deaths'])/7)

df['new_cases_normalized']=cases
df['new_deaths_normalized']=deaths

df.set_index("date",inplace=True)
df.to_pickle('canada_data.pkl') 