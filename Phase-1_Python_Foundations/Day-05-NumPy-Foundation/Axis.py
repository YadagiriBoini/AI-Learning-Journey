import numpy as np

data = np.array([
    [10, 20, 30],
    [40, 50, 60]
])


print(np.mean(data))

# Mean by column
print(np.mean(data, axis=0))

# Mean by rows
print(np.mean(data, axis=1))