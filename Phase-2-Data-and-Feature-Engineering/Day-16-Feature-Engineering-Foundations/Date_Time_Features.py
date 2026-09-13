import pandas as pd

data = {
    "age": [20, 25, 30, 35, 40],
    "salary": [20000, 30000, 50000, 70000, 100000],
    "experience": [1, 2, 5, 8, 15],
    "Date": ["2021-01-10", "2022-03-15", "2023-06-20", "2024-08-25", "2025-12-30"]
}

df = pd.DataFrame(data)

df["Date"] = pd.to_datetime(df["Date"])

# Extract
df["Year"] = df["Date"].dt.year
df["Month"] = df["Date"].dt.month
df["Day"] = df["Date"].dt.day
df["Day_Of_Week"] = df["Date"].dt.dayofweek
    
print(df)