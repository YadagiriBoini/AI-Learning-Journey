# Label encoding = useful when the categories have an actual order.

from sklearn.preprocessing import LabelEncoder
import pandas as pd

data = {
    "Age":[21,25,30],
    "City":["Hyd","Dl","Mb"],
    "Gender":["M","F","M"],
    "Salary":[25000,35000,50000]
}

df = pd.DataFrame(data)

encoder = LabelEncoder()

df["Gender_Encode"] = encoder.fit_transform(df['Gender'])
df["City_Encode"] = encoder.fit_transform(df["City"])

print(df)