# Import Libraries
import numpy as np
import pandas as pd
import warnings
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Ignore the warnings
warnings.filterwarnings("ignore",category=UserWarning)

# Load data
df = pd.read_csv("Day-26-Linear-Regression\salary_data.csv")

X = df.iloc[:,[0]]
y = df.iloc[:,1]

# Checking Shape
print("Shape of X:",X.shape)
print("Shape of y:",y.shape)

# Create model
model = LinearRegression()

# Train model
model.fit(X,y)

# Coefficicent and intercept
print("Coefficient:",model.coef_)
print("Intercept:",model.intercept_)

# Prediction for new data
new_data = np.array([[12.5]])
prediction = model.predict(new_data)
print("Prediction for 12.5:",prediction)

# Calculating MSE
y_pred = model.predict(X)
mse = mean_squared_error(y, y_pred)
print("MSE:",mse)

# Visualize 
plt.scatter(X,y, color="blue", label="Actual_Data")
plt.plot(X,y_pred, color="Red", label="Regression_Line")
plt.xlabel("Experience")
plt.ylabel("Salary")
plt.legend()
plt.show()

