import numpy as np

matrix = np.array([
    [1,2,3],
    [4,5,6]
])

flat = matrix.flatten()   # copy
print(flat)

print(matrix.ravel())     # usually view when possible
