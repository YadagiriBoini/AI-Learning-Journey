import pandas as pd

df = pd.DataFrame({
    "name": ["A", "B", "C", "B"],
    "age": [20, 21, 22, 21],
    "salary": [25000, 30000, 35000, 30000]
})



df1 = df.drop_duplicates(
    subset=["name"]
)
print(df1)


# Keeping the last record
df2 = df.drop_duplicates(
    subset=["name"],
    keep="last"
)
# Reseting index
df2 = df2.reset_index(drop=True)
print(df2)


# Removing all duplcaited rows
df3 = df.drop_duplicates(
    subset=["name"],
    keep=False
)
# Resetting index
df3 = df3.reset_index(drop=True)
print(df3)