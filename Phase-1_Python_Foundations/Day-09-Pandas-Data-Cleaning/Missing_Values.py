import pandas as pd

data = {
    "Name": ["Ravi", "Anand", "Raj", "Priya", "Kiran", "Ravi"],
    "Age": [22, 25, None, 27, 24, 22],
    "Salary": [35000, 50000, 28000, None, 45000, 35000],
    "City": ["Hyderabad", "Chennai", "Delhi", "Hyderabad", None, "Hyderabad"]
}

df = pd.DataFrame(data)


# Detect missing value
print(df.isnull())  #df.isna()


# Count missing values
print( df.isnull().sum())


# Checking missing values
print( df.isnull().any() )         # Checks for each column
print( df.isnull().values.any() )  # Check for entire dataframe

