import pandas as pd

def clean_data(df):
    df = df.drop_duplicates()
    df = df.reset_index(drop=True)
    return df

df = pd.DataFrame({
    "name": ["Alice", "Bob", "Charlie", "Bob", "David"],
    "age": [22, 25, 30, 25, 28],
    "salary": [30000, 40000, 50000, 40000, 45000]
})

cleaned_df = clean_data(df)
print(cleaned_df)