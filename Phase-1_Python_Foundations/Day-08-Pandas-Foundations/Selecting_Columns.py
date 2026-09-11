
import pandas as pd

data = {
    "Name": ["Ravi", "Anand", "Raj", "Priya"],
    "Age": [20, 21, 19, 22],
    "Marks": [85, 92, 76, 88]
}

df = pd.DataFrame(data)


print(df)


print(df.columns)           # Column names
print(df.columns.tolist())  # Converts column's names into a list 



print( df["Marks"] )           # Selecting a column
print( df[["Name", "Marks"]])  # Selecting multiple columns

