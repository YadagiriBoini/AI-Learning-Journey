import pandas as pd

data = {
    "Name": ["Ravi", "Anand", "Raj", "Priya", "Kiran", "Ravi"],
    "Age": [22, 25, None, 27, 24, 22],
    "Salary": [35000, 50000, 28000, None, 45000, 35000],
    "City": ["Hyderabad", "Chennai", "Delhi", "Hyderabad", None, "Hyderabad"]
}

df = pd.DataFrame(data)


# To know the duplicates in the dataframe
print( df.duplicated() )          # Returns bool value for each row
print( df.duplicated().sum() )    # Returns number of duplicated values

