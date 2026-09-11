import pandas as pd

data = {
    "Name": ["Ravi", "Anand", "Raj", "Priya", "Kiran", "Ravi"],
    "Age": [22, 25, None, 27, 24, 22],
    "Salary": [35000, 50000, 28000, None, 45000, 35000],
    "City": ["  Hyderabad  ", "chennai", "DL", "Hyd", None, "HYDERABAD"]
}

df = pd.DataFrame(data)

df["Age"] = df["Age"].fillna( df["Age"].mean() )
df["Salary"] = df["Salary"].fillna( df["Salary"].median() )
df["City"] = df["City"].fillna( df["City"].mode()[0] )

df["Age"] = df["Age"].astype(int)



# Cleaning a String Values
df["City"] = df["City"].str.strip()
df["City"] = df["City"].str.lower()
print(df)