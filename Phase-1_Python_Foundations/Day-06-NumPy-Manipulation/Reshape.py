import numpy as np

arr = np.arange(1,13)

matrix1 = arr.reshape(3,-1)
matrix2 = arr.reshape(-1,3)

print(matrix1)   # 3 Rows, Remaining all columns
print(matrix2)   # all rows, 3 Columns