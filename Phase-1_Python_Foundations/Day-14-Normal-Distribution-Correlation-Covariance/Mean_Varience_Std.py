import numpy as np

data = np.array([2,4,6,8,10])


mean = np.mean(data)               # Mean is the average
varience = np.var(data)            # How spread out are the values from the mean?
std = np.std(data)                 # square root of variance


print("Mean:",mean)
print("Varience:",varience)
print("Standard Deviation:",std)   
 # Low std => Values close together      # High std => Values spread out