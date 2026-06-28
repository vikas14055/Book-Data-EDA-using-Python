import matplotlib.pyplot as plt

import pandas as pd

df = pd.read_csv("books_dataset.csv")

print(df.head())

print(df.info())

df["Price"] = df["Price"].str.replace("Â£", "", regex=False)
df["Price"] = df["Price"].str.replace("£", "", regex=False)

df["Price"] = pd.to_numeric(df["Price"], errors="coerce")

print("\nStatistics:")
print(df["Price"].describe())


print("\nMost Expensive Book:")
print(df.loc[df["Price"].idxmax()])

print("\nCheapest Book:")
print(df.loc[df["Price"].idxmin()])

print("\nAverage Price:")
print(df["Price"].mean())

print("\nHypothesis Test:")

if df["Price"].mean() > 30:
    print("Average book price is above £30")
else:
    print("Average book price is £30 or below")

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Records:")
print(df.duplicated().sum())

plt.hist(df["Price"])

plt.title("Book Price Distribution")
plt.xlabel("Price")
plt.ylabel("Frequency")

plt.show()