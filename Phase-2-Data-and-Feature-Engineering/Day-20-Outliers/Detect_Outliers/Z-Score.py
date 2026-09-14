import numpy as np
from scipy.stats import zscore

data = np.array([10, 12, 11, 13, 14, 15, 12, 11, 100])


Z_Score = (data - np.mean(data)) / np.std(data)
z_score = zscore(data)

print("Using Numpy:",Z_Score) 
print("Using Scipy:",z_score)

outlier = data[ np.abs(z_score) > 3]
print(outlier)