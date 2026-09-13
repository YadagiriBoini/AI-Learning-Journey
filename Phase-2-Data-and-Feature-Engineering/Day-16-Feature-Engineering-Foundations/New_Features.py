import pandas as pd

data = {
    "age": [20, 25, 30, 35, 40],
    "salary": [20000, 30000, 50000, 70000, 100000],
    "experience": [1, 2, 5, 8, 15]
}

df = pd.DataFrame(data)

df["Sal_Per_Year_Exp"] = df["salary"]/df["experience"]

print(df)