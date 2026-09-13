import pandas as pd

data = {
    "age": [20, 25, 30, 35, 40],
    "salary": [20000, 30000, 50000, 70000, 100000],
    "experience": [1, 2, 5, 8, 15]
}

df = pd.DataFrame(data)


# Derived features:
df["Total"] = df["age"]+df["experience"]            # Addition
df["Age_Minus_Exp"] = df["age"]-df["experience"]    # Difference
df["Age_Exp"] = df["age"]*df["experience"]          # Multiplication
df["Sal_Per_Exp"] = df["salary"] / df["experience"] # Ratio

print(df)