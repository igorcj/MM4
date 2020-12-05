#!/usr/bin/env python3
# retira os dados do governo canadense e filtra colunas de interesse agrupando apenas para quebec e ontario

import wget, os, pandas as pd
url = "https://health-infobase.canada.ca/src/data/covidLive/covid19-download.csv"
filename = wget.download(url)
print()

df = pd.read_csv(filename)
os.remove(filename)

df.query('prname in ["Ontario","Quebec"]', inplace=True)
df.drop(columns=['pruid', 'prname', 'prnameFR', 'numconf', 'numprob', 'numdeaths', 'numtotal', 'numtested',
       'percentrecover', 'ratetested', 'numtoday', 'percentoday',
       'ratetotal', 'ratedeaths', 'numdeathstoday', 'percentdeath',
       'numtestedtoday', 'numrecoveredtoday', 'percentactive', 'numactive',
       'rateactive', 'numtotal_last14', 'ratetotal_last14', 'numdeaths_last14',
       'ratedeaths_last14', 'avgincidence_last7','avgratedeaths_last7'], inplace=True)
df["date"] = pd.to_datetime(df["date"])
df.sort_values(by=['date'],inplace=True)

date=df['date'].unique()
avg7=[df.loc[df['date'] == day, 'avgtotal_last7'].sum() for day in date]
dead7=[df.loc[df['date'] == day, 'avgdeaths_last7'].sum() for day in date]
recover=[df.loc[df['date'] == day, 'numrecover'].sum() for day in date]

df=pd.DataFrame({'date':date,'cases_normalized':avg7,'deaths_normalized':dead7,'recovers':recover})
df.set_index('date', drop=True, inplace=True)

df.to_pickle('canada_data.pkl')