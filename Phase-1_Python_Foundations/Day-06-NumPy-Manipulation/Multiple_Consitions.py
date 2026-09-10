import numpy as np

scores = np.array([35, 45, 55, 65, 75, 85, 95])

print( scores[(scores>=50) & (scores<=80)] )  # With numpy always use &,|
print( scores[(scores<40)  | (scores>90)] )