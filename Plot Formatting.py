import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("https://www.sololearn.com/uploads/ca-covid.csv")

df.drop('state', axis=1, inplace=True)
df['date'] = pd.to_datetime(df['date'], format="%d.%m.%y")
df['month'] = df['date'].dt.month
df['day'] = df['date'].dt.day
df.set_index('day', inplace=True)

df = df[df['month'] == 6]

df[['cases', 'deaths']].plot(kind="line", legend=True)
plt.xlabel('Days in June')
plt.ylabel('Number')
plt.savefig('plot11.png')
