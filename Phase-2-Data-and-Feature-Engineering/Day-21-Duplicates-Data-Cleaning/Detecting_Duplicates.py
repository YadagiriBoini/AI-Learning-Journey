import pandas as pd

df = pd.DataFrame({
    "name": ["A", "B", "C", "B"],
    "age": [20, 21, 22, 21],
    "salary": [25000, 30000, 35000, 30000]
})

print(df)


# Detecting Duplicates
print(df.duplicated())    # Returns a boolean value


# Counting Duplicates
print(df.duplicated().sum())   # Returns the number of dulicates


# To view Duplicates
duplicate = df[df.duplicated()]
print(duplicate)