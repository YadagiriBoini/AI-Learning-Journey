import pandas as pd

data = {
    "age": [18, 21, 25, 30, 35],
    "height": [165, 170, 175, 172, 180],
    "weight": [60, 68, 75, 80, 90],
    "study_hours": [2, 4, 5, 7, 8]
}

df = pd.DataFrame(data)

df["Height_In_Cm"] = df["height"]/100             # Height inn centimeters
df["BMI"] = df["weight"]/(df["Height_In_Cm"])**2  # BMI
df["Study_Eff"] = df["study_hours"]/df["age"]     # Study Efficiency
df["Age_sqaure"] = df["age"]**2                   # Age square
df["HW"] = df["height"]*df["weight"]              # Height-weight interaction

print(df)