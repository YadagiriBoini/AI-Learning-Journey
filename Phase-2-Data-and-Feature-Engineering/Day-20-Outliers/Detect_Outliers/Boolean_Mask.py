import pandas as pd

df = pd.DataFrame({
     "salary": [25000, 27000, 30000, 32000, 35000, 36000, 38000, 40000, 155555]
})

q1 = df["salary"].quantile(0.25)
q3 = df["salary"].quantile(0.75)
IQR = q3-q1

lower = q1-1.5*IQR
upper = q3+1.5*IQR

mask = ( df["salary"] < lower ) | ( df["salary"] > upper )

print(mask)