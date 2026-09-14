import pandas as  pd
from sklearn.preprocessing import StandardScaler

data = {
    "age": [20, 25, 30, 35, 40],
    "salary": [20000, 40000, 60000, 80000, 100000],
    "experience": [1, 3, 5, 7, 10]
}

df = pd.DataFrame(data)

scaler = StandardScaler()

scaled_df = scaler.fit_transform(df)

print(scaled_df)