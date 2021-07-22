import pandas as pd
print("** Data Frames **")
print("\n* #1 *")
data = {
    'ages': [14, 18, 24, 42],
    'heights': [165, 180, 176, 184]
}
df = pd.DataFrame(data)
print("\n", df)

#    ages  heights
# 0    14      165
# 1    18      180
# 2    24      176
# 3    42      184

print("\n* #2 *")
x = {
    'a': [1, 2],
    'b': [3, 4],
    'c': [5, 6]
}

df = pd.DataFrame(x)
print("\n", df)

#    a  b  c
# 0  1  3  5
# 1  2  4  6


print("\n* #3 *")

data = {
    'ages': [14, 18, 24, 42],
    'heights': [165, 180, 176, 184]
}

df = pd.DataFrame(data, index=['James', 'Bob', 'Amy', 'Dave'])
print(df)
print("\n", df.loc["Bob"])

#        ages  heights
# James    14      165
# Bob      18      180
# Amy      24      176
# Dave     42      184

# Bob:
# ages        18
# heights    180
# Name: Bob, dtype: int64
print("\n* #4 - Indexing *")

print("\n", df["ages"])
print("\n", df[["ages", "heights"]])

print("\n* #5 - slicing-iloc *")
data = {
    'ages': [14, 18, 24, 42],
    'heights': [165, 180, 176, 184]
}

df = pd.DataFrame(data, index=['James', 'Bob', 'Amy', 'Dave'])

# third row
print("\n", df.iloc[2])
# first 3 rows
print("\n", df.iloc[:3])
# rows 2 to 3
print("\n", df.iloc[1:3])

print("\n* #6 - slicing-Conditions *")
print("\n", df[(df['ages'] > 18) & (df['heights'] > 180)])

print("\n* #6 - Reading data *")
df = pd.read_csv("https://www.sololearn.com/uploads/ca-covid.csv")
#  wget -o .\ca-covid.csv https://www.sololearn.com/uploads/ca-covid.csv
# print("\n", df.head()) # devolve 5 linhas
# Similarly, you can get the last rows using the tail() function.
print("\n", df.head(50))  # primeiras x linhas

print("\n* #6 - Reading data-Info *")

print("\n", df.info)

print("\n* #7 - Reading data-Index Columns *")

df.set_index('date', inplace=True)
print("\n", df.info)

print("\n* #8 - Reading data-Dropping Columns *")
df.drop('state', axis=1, inplace=True)
print("\n", df.info)

print("\n* #9 - Creating Columns *")
df = pd.read_csv("https://www.sololearn.com/uploads/ca-covid.csv")
df.drop('state', axis=1, inplace=True)
df['month'] = pd.to_datetime(df['date'], format="%d.%m.%y").dt.month_name()
df.set_index('date', inplace=True)
print(df.head())

print("\n* #10 - Summary Statistics *")
print("* All  *")
print("\n", df.describe())
print("\n* Cases *")
print("\n", df['cases'].describe())

print("\n* #11 - Grouping *")
# value_counts() returns how many times a value appears in
# the dataset, also called the frequency of the values.
print(df['month'].value_counts())

print("\nCases by Month: \n")
print(df.groupby('month')['cases'].sum())
print("\nTotal Cases:")
print(df['cases'].sum())
