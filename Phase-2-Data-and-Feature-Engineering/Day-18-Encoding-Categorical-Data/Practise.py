import pandas as pd
from sklearn.preprocessing import OneHotEncoder

data = {
    "age": [21, 25, 30, 35, 40],
    "city": ["Hyderabad","Delhi","Mumbai","Hyderabad","Delhi"],
    "gender": ["Male","Female","Male","Female","Male"]
}

df = pd.DataFrame(data)

encoder = OneHotEncoder(
    sparse=False,
    handle_unknown="ignore"
)

encoded = encoder.fit_transform(
    df[["city","gender"]]
)

print(encoded)
print(encoder.categories_)