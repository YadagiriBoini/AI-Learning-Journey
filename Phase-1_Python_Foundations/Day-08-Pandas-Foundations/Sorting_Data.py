
import pandas as pd

data = {
    "Name": ["Ravi", "Anand", "Raj", "Priya"],
    "Age": [20, 21, 19, 22],
    "Marks": [85, 92, 76, 88]
}

df = pd.DataFrame(data)

df_sorted = df.sort_values("Marks")  # Ascending  (by default)
df_sorted_des = df.sort_values("Marks", ascending=False)  # Descending

print(df_sorted)
print(df_sorted_des)