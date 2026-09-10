import numpy as np

data = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

print(np.mean(data))  # Mean of entire data

print(np.mean(data, axis=0))   # Mean of every column
print(np.mean(data, axis=1))   # Mean of every row



print([
np.sum(data, axis=0),
np.mean(data, axis=0),
np.std(data, axis=0),
np.min(data, axis=0),
np.max(data, axis=0)
])