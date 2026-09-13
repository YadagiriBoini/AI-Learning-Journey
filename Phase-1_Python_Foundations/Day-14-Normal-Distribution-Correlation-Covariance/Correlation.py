# Correlation => How strongly and in what direction two variables are linearly related

import numpy as np

hours = np.array([1,2,3,4,5])
marks = np.array([40,50,60,70,80])

correlation_matrix = np.corrcoef(hours,marks)

print(correlation_matrix)
