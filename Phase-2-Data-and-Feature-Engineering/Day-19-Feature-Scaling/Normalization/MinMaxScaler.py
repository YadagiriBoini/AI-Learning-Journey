import pandas as pd
from sklearn.preprocessing import MinMaxScaler

data = {
    "age": [20, 25, 30, 35, 40],
    "salary": [20000, 40000, 60000, 80000, 100000],
    "experience": [1, 3, 5, 7, 10]
}

df = pd.DataFrame(data)

scaler = MinMaxScaler()

scaled_data = scaler.fit_transform(df)
print(scaled_data)