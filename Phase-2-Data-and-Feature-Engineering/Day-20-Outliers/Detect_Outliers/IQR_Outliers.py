import pandas as pd

df = pd.DataFrame({
    "salary": [25000, 27000, 30000, 32000, 35000, 36000, 38000, 40000, 155555]
})

Q1 = df["salary"].quantile(0.25)
Q3 = df["salary"].quantile(0.75)
IQR = Q3-Q1

print("Q1:",Q1)
print("Q3:",Q3)
print("IQR:",IQR)


# Boundaries
lower = Q1-1.5*IQR
upper = Q3+1.5*IQR
outlier = df[ (df["salary"] < lower) | (df["salary"] > upper) ]

print("Lower:",lower)
print("Upper:",upper)
print("Outlier:",outlier)