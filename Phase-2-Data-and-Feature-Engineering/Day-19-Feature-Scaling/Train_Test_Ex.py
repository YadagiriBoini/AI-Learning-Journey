import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

data = {
    "age": [20, 25, 30, 35, 40],
    "salary": [20000, 40000, 60000, 80000, 100000],
    "experience": [1, 3, 5, 7, 10]
}

df = pd.DataFrame(data)

X_train, X_test, = train_test_split(
    df,
    test_size=0.2,
    random_state=42
)

sacler = StandardScaler()

X_train_Scale = sacler.fit_transform(X_train)
X_test_Scale = sacler.transform(X_test)

print(X_train_Scale)
print(X_test_Scale)