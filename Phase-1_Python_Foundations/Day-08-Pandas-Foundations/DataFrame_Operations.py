import pandas as pd

data = {
    "Name": ["Ravi", "Anand", "Raj", "Priya"],
    "Age": [20, 21, 19, 22],
    "Marks": [85, 92, 76, 88]
}

df = pd.DataFrame(data)

print(df)
print(df.shape)  # Shape in rows and columns

print(df.head()) # First 5 rows of the data
print(df.head(2)) # First 2 rows of the data

print(df.tail()) # Last 5 rows of the data
print(df.tail(2)) # Last 2 rows of the data


