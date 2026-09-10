import  numpy as np

a = np.array([1,2,3])
b = np.array([4,5,6])

c = np.array([
    [1,2,3],
    [4,5,6]
])
d = np.array([
    [7,8,9],
    [2,4,6]
])



print(np.concatenate([a,b])) # 1D Arrays
print(np.concatenate([c,d], axis=0)) # 2D Arrays   axis=0=> Columns Wise  
print(np.concatenate([c,d], axis=1)) # axis=1=> Row wise

# Insted of axis=0/1 we can use vstack, hstack
print(np.vstack([c,d]))  # Vertical/Column
print(np.hstack([c,d]))  # Horizontal/Row