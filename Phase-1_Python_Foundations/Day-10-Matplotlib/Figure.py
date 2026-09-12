import matplotlib.pyplot as plt

x = [1,2,3,4]
y = [10,20,15,25]

plt.figure(figsize=(8,5))  #To control the width and height of the chart shown (8-width, 5-height)
plt.plot(x,y)
plt.show()





# It becomes especially useful when you have multiple separate plots
plt.figure(figsize=(6, 4))
plt.plot([1, 2, 3], [10, 20, 30])
plt.title("Plot 1")

plt.figure(figsize=(6, 4))
plt.plot([1, 2, 3], [30, 20, 10])
plt.title("Plot 2")

plt.show()