# Imputation = Replacing missing values with reasonable values

import pandas as pd

data = {
    "age": [21, 25, None, 32],
    "salary": [25000, None, 50000, 70000],
    "experience": [1, 3, 5, None],
    "city":["Hyderabad",None,"Hyderabad","Chennai"]
}

df = pd.DataFrame(data)

# Constant Values -> replace missing values with a fixed value
df["age"] = df["age"].fillna(0)
df["city"] = df["city"].fillna("Unknown")

print(df)