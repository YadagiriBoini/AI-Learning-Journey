import pandas as pd

data = {
    "Name": ["Ravi", "Anand", "Raj", "Priya"],
    "Age": [20, 21, 19, 22],
    "Marks": [85, 92, 76, 88]
}

df = pd.DataFrame(data)


print(df.describe())  # count, mean, std, min, 25%, 50%, 75%, max

print(df.info())      # index, column_names, null_values, Datatype of columns, memory_useage

print(df.dtypes)      # Datatype of the columns