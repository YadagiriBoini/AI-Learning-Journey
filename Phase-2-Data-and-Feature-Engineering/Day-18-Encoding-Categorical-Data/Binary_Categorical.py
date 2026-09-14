
import pandas as pd
from sklearn.preprocessing import OneHotEncoder

data = {
    "Age":[21,25,30],
    "City":["Hyd","Dl","Mb"],
    "Gender":["M","F","M"],
    "Salary":[25000,35000,50000],
    "Purchased":["Yes","No","Yes"]
}

df = pd.DataFrame(data)

df["Purchased_bin"] = df["Purchased"].map({
    "Yes":1,
    "No":0
})

print(df)