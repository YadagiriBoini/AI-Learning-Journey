from sklearn.preprocessing import RobustScaler
import pandas as pd

df = pd.DataFrame({
     "salary": [25000, 27000, 30000, 32000, 35000, 36000, 38000, 40000, 155555]
})

scaler = RobustScaler()

scaled_df = scaler.fit_transform(df[["salary"]])

print(scaled_df)