import pandas as pd
from sklearn.impute import SimpleImputer

data = {
    "age": [21, 25, None, 32],
    "salary": [25000, None, 50000, 70000],
    "experience": [1, 3, 5, None]
}

df = pd.DataFrame(data)

imputer = SimpleImputer(strategy="mean")

df[["age","salary","experience"]] = imputer.fit_transform(
    df[["age","salary","experience"]]
)

print(df)