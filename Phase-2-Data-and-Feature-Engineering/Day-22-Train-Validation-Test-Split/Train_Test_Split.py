import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

X = np.array([[20],[21],[22],[23],[24],[25],[26],[27],[28],[29]])
y = np.array([0,0,0,1,1,1,1,1,1,1])

X_train, X_test, y_train, y_test = train_test_split( X, y, test_size=0.2, random_state=42 )

print(X_train.shape)
print(X_test.shape)

print(y_train.shape)
print(y_test.shape)