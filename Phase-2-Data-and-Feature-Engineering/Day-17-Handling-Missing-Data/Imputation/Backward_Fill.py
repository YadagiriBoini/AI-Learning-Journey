# Imputation = Replacing missing values with reasonable values

import pandas as pd

data = {
    "age": [21, 25, None, 32],
    "salary": [25000, None, 50000, 70000],
    "experience": [1, 3, 5, None],
    "city":["Hyderabad",None,"Hyderabad","Chennai"]
}

df = pd.DataFrame(data)

# ForwardFill -> It uses the next available value
df["age"] = df["age"].bfill()
df["salary"] = df["salary"].bfill()

print(df)