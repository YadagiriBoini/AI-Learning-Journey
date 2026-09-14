# OneHotEncoding = handles unseen categories rather than crashing

import pandas as pd
from sklearn.preprocessing import OneHotEncoder

data = {
    "Age":[21,25,30],
    "City":["Hyd","Dl","Mb"],
    "Gender":["M","F","M"],
    "Salary":[25000,35000,50000],
    "Level":["Low","Medium","High"]
}

df = pd.DataFrame(data)

# Manual way
# encode_df = pd.get_dummies(
#     df,
#     columns=["City"]
# )
# print(encode_df)



encoder = OneHotEncoder(
    drop="first",               # Even if the column drops encoder adjusts
    handle_unknown="ignore",    # Even If new data is encountered program would not crash
    sparse=False                
)

encoded = encoder.fit_transform(
    df[["City"]]
)

print(encoded)