import pandas as pd

df = pd.DataFrame({
    "name": ["A", "B", "C", "B"],
    "age": [20, 21, 22, 21],
    "salary": [25000, 30000, 35000, 30000]
})


print(df.duplicated(keep="first"))

print()

print(df.duplicated(keep="last"))

print()

print(df.duplicated(keep=False))

print()

# To view all duplicates record
duplicate = df[df.duplicated(keep=False)]
print(duplicate)