import numpy as np

scores = np.array([35, 45, 55, 65, 75, 85, 95])

res1 = np.where( scores>=60, "Pass", "Fail" )   # Return Bool Value
res2 = np.where( scores>=60 )

print(res1)
print(res2)