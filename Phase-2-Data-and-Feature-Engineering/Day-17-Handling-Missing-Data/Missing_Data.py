import pandas as pd

data = {
    "age": [21, 25, None, 32],
    "salary": [25000, None, 50000, 70000],
    "experience": [1, 3, 5, None]
}

df = pd.DataFrame(data)

# Detect missing values
# print(df.isnull())

# Counting missing values
print(df.isnull().sum())        # df.isna().sum()


print( df[df.isnull().any(axis=1)] )