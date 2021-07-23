from datetime import date
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("./ca-covid.csv")

df.drop('state', axis=1, inplace=True)
df.set_index('date', inplace=True)
df['ratio'] = df['deaths']/df['cases']
print(df)
#racio = df['ratio'].max()
#print(df[(df['ratio'] == racio)])
s = pd.Series(df['cases'])
s.plot(kind='bar')
# plt.savefig('covid.png')
