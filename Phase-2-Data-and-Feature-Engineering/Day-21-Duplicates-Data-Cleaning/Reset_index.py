import pandas as pd

df = pd.DataFrame({
    "name": ["Alice", "Bob", "Charlie", "Bob", "David"],
    "age": [22, 25, 30, 25, 28],
    "salary": [30000, 40000, 50000, 40000, 45000]
})

df = df.drop_duplicates()

# Reseting index
df = df.reset_index(drop=True)
print(df)