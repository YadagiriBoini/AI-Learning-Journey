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

df["City"] = df["City"].str.strip()
df["City"] = df["City"].str.lower()


df["Salary_Level"] = "Low"
df.loc[ df["Salary"] >= 30000, "Salary_Level"] = "Medium"
df.loc[ df["Salary"] >= 50000, "Salary_Level"] = "High"


df["City"] = df["City"].replace(
    { "hyd":"hyderabad",
      "dl": "delhi",
      "cn": "chennai"
    }
)


cc = {
    "hyderabad":1,
    "delhi":2,
    "chennai":3
    }
df["City_Code"] = df["City"].map(cc)



df["Salary_Lakh"] = df["Salary"].apply(
    lambda x: x/100000
)



# Renaming a column
df = df.rename( columns={ "Salary_Level":"Salary_Category" })

print(df)