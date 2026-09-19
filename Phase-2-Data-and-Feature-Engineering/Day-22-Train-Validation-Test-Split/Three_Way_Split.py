import numpy as np
from sklearn.model_selection import train_test_split

X = np.array([[20],[21],[22],[23],[24],[25],[26],[27],[28],[29]])
y = np.array([0,0,0,1,1,1,1,1,1,1])


# 70% → Training  30% → Temporary
X_train, X_temp, y_train, y_temp = train_test_split(X, y, test_size=0.2, random_state=42)

# Spliting temporary data
X_test, X_val, y_test, y_val = train_test_split( X_temp, y_temp, test_size=0.5, random_state=42)


print(X_train.shape)
print(X_test.shape)
print(X_val.shape)