import numpy as np

matrix = np.array([
    [1,  2,  3,  4],
    [5,  6,  7,  8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
])

# matirx[ row, column ]


# Rows
print(matrix[0])   # First row
print(matrix[-1])  # Last row

# Columns
print(matrix[:,0]) # First column
print(matrix[:,-1]) # Last Column


print()
print()


# Submatrix
# Rows
print(matrix[:2])  # Frist 2 rows

# Columns
print(matrix[:,:2])  # First 2 columns


print()
print()


print(matrix[:2,:2])  # First two rows and first two columns
print(matrix[1:3,1:3]) # middle section