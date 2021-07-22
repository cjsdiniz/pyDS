import pandas as pd
print("** Data Frames **")
print("\n* #1 *")
data = {
    'ages': [14, 18, 24, 42],
    'heights': [165, 180, 176, 184]
}
df = pd.DataFrame(data)
print(df)

print("\n* #2 *")
x = {
    'a': [1, 2],
    'b': [3, 4],
    'c': [5, 6]
}

df = pd.DataFrame(x)
print(df)

print("\n* #3 *")

data = {
    'ages': [14, 18, 24, 42],
    'heights': [165, 180, 176, 184]
}

df = pd.DataFrame(data, index=['James', 'Bob', 'Amy', 'Dave'])
print(df)
print("\n", df.loc["Bob"])
