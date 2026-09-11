import pandas as pd

data = {
    "Name": ["Ravi", "Anu", "Raj", "Priya"],
    "Age": [20, 21, 19, 22],
    "Marks": [85, 92, 76, 88]
}

df = pd.DataFrame(data)

print(df)