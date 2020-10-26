#!/usr/bin/env python3
# retira os dados do governo canadense e filtra colunas de interesse agrupando apenas para quebec e ontario

import wget, os, pandas as pd, numpy as np
#url1 = "https://health-infobase.canada.ca/src/data/covidLive/covid19-download.csv"
#covid_file = wget.download(url1)
covid_file = "covid19-download.csv"
df = pd.read_csv(covid_file)

#url2 = "https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/gmobility/Google Mobility Trends (2020).csv"
#mobility_file = wget.download(url2)
#mobility_file = "Google Mobility Trends (2020).csv"
#df2 = pd.read_csv(mobility_file)

df.query('prname in ["Ontario","Quebec"]', inplace=True)

#df.drop(columns=['pruid', 'prname', 'prnameFR', 'numconf', 'numprob', 'numdeaths', 'numtotal', 'numtested',
#       'percentrecover', 'ratetested', 'numtoday', 'percentoday',
#       'ratetotal', 'ratedeaths', 'numdeathstoday', 'percentdeath',
#       'numtestedtoday', 'numrecoveredtoday', 'percentactive', 'numactive',
#       'rateactive', 'numtotal_last14', 'ratetotal_last14', 'numdeaths_last14',
#       'ratedeaths_last14', 'avgincidence_last7','avgratedeaths_last7'], inplace=True)

df["date"] = pd.to_datetime(df["date"])
df.sort_values(by=['date'],inplace=True)

date    = df['date'].unique()

tcases  = [df.loc[df['date'] == day, 'numconf'].sum() for day in date]
ncases  = np.append([0], np.diff(tcases))

tdeaths = [df.loc[df['date'] == day, 'numdeaths'].sum() for day in date]
ndeaths = np.append([0], np.diff(tdeaths))

df = pd.DataFrame({'date':date, 'tcases':tcases, 'ncases':ncases, 'tdeaths':tdeaths, 'ndeaths':ndeaths})
df.set_index('date', drop=True, inplace=True)

df.to_pickle('canada_data.pkl')

#os.remove(filename)
