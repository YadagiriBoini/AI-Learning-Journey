# Ordinal Encoder = Categories have a meaningful order

import pandas as pd
from sklearn.preprocessing import OrdinalEncoder

data = {
    "Age":[21,25,30],
    "City":["Hyd","Dl","Mb"],
    "Gender":["M","F","M"],
    "Salary":[25000,35000,50000],
    "Level":["Low","Medium","High"]
}

df = pd.DataFrame(data)

encoder = OrdinalEncoder()

df[["Level_Encode"]] = encoder.fit_transform(df[["Level"]])

print(df)
