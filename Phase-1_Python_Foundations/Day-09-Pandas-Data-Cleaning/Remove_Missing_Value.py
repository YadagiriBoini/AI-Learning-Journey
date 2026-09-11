import pandas as pd

data = {
    "Name": ["Ravi", "Anand", "Raj", "Priya", "Kiran", "Ravi"],
    "Age": [22, 25, None, 27, 24, 22],
    "Salary": [35000, 50000, 28000, None, 45000, 35000],
    "City": ["Hyderabad", "Chennai", "Delhi", "Hyderabad", None, "Hyderabad"]
}

df = pd.DataFrame(data)

df_clean  = df.dropna()   # Removes rows containing missing value

print(df_clean)