
import pandas as pd

data = {
    "Name": ["Ravi", "Anand", "Raj", "Priya"],
    "Age": [20, 21, 19, 22],
    "Marks": [85, 92, 76, 88]
}

df = pd.DataFrame(data)


print( df.iloc[0] )  # First row
print( df.iloc[1])   # Second row


# Selecting multiple rows
print( df.iloc[0:2])  # Row 0, Row 1


# Selecting Specific row and column
print( df.iloc[0,2])  # 0 rows and 2 columns