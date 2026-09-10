import numpy as np

matrix = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])  # can change dtype = float


print(matrix)
print(matrix.ndim)   # 2 D
print(matrix.shape)  # 3 rows, 3 columns
print(matrix.size)   # 9
print(matrix.dtype)  # int32