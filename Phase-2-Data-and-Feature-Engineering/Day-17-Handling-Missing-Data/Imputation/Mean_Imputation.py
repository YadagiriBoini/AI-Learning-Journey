# Imputation = Replacing missing values with reasonable values

import pandas as pd

data = {
    "age": [21, 25, None, 32],
    "salary": [25000, None, 50000, 70000],
    "experience": [1, 3, 5, None]
}

df = pd.DataFrame(data)

print(df.isnull().sum())

df["age"] = df["age"].fillna(df["age"].mean())

print(df)