import numpy as np

Matrix_A = np.array([
    [1,2],
    [3,4]
])

Matrix_B = np.array([
    [5,6],
    [7,8]
])

print(Matrix_A.shape)   # 2,2
print(Matrix_B.shape)   # 2,2

print( Matrix_A + Matrix_B )     # Matrix Addition
print( Matrix_A * Matrix_B )     # Matrix Element-wise Multiplication
print( Matrix_A @ Matrix_B )     # Matrix Multipication
print( Matrix_A.T )              # Matrix Transpose