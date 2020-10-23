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

df.to_csv('canada_data.csv', index=False) 