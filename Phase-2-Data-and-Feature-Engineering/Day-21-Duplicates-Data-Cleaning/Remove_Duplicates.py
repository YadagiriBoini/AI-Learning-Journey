import pandas as pd

df = pd.DataFrame({
    "name": ["A", "B", "C", "B"],
    "age": [20, 21, 22, 21],
    "salary": [25000, 30000, 35000, 30000]
})

df_clean = df.drop_duplicates()   # No change in the original Dataframe
print(df_clean)

# df_cleaned = df.drop_duplicates(inplace=True)
# print(df_cleaned)