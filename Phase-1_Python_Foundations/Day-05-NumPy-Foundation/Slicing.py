import numpy as np

arr1 = np.array([10, 20, 30, 40, 50])
matrix = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])


print(arr1[1:4])  # [20,30,40]
print(matrix[:2]) # First 2 rows 
print(matrix[:,:2]) # Frist 2 columns