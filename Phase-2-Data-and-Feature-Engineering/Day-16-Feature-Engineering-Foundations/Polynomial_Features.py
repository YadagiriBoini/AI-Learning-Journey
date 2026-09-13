import pandas as pd

data = {
    "age": [20, 25, 30, 35, 40],
    "salary": [20000, 30000, 50000, 70000, 100000],
    "experience": [1, 2, 5, 8, 15]
}

df = pd.DataFrame(data)


# Polynomial Feature
df["Age_Square"] = df["age"]**2

print(df)