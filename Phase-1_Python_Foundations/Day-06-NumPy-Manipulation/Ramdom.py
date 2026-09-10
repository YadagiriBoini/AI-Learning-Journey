import numpy as np


print(np.random.rand(5)) # Creates 5 random numbers between 1 to 5
print(np.random.rand(3,4)) # creates 3*4 random values


print(np.random.randint(1,10, size=5))

np.random.seed(42)
print(np.random.randint(1,10,size=5)) #will produce the same sequence each time you run it with that seed