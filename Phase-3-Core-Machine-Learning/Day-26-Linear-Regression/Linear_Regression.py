# Import Libraries
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Load data
X = np.array([1,2,3,4,5]).reshape(-1,1)  # features X to generally have 2 dimensions (number of samples × number of features)
y = np.array([35,42,50,58,67])

# Create model
model = LinearRegression()

# Train model
model.fit(X,y)

# Visualize data
plt.scatter(X,y)
plt.xlabel("Study_Hours")
plt.ylabel("Exam_Score")
plt.title("Hours vs Marks")
plt.show()

# Check  cofficient
print(model.coef_[0])
print(model.intercept_)

# New Prediction
new_data = np.array([[6]])
predict = model.predict(new_data)
print(predict)

y_pred = model.predict(X)

# Regression line
plt.scatter(X,y, color="blue", label="Actual_Data")
plt.plot(X, y_pred, color="red", label="Regression_Line")
plt.xlabel("Hours_Studied")
plt.ylabel("Exam Score")
plt.title("Linear Regression")
plt.legend()
plt.show()