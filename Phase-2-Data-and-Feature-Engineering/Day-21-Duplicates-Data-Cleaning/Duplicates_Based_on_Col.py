import pandas as pd

df = pd.DataFrame({
    "name": ["A", "B", "C", "B"],
    "age": [20, 21, 22, 21],
    "salary": [25000, 30000, 35000, 30000]
})

print(df.duplicated(subset=["name"]))
print(df.duplicated(subset=["age"]))

#  Combination of columns
print(df.duplicated(subset=["name","age","salary"]))