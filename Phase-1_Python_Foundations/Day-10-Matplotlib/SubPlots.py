import matplotlib.pyplot as plt

x = [1,2,3,4]
y = [10,20,15,25]

plt.figure(figsize=(14,6))   # Width, Height

plt.subplot(1,3,1)           # subplot(rows, columns, position) ( 1 row, 2 columns, position 1 )
plt.plot(x,y)
plt.xlabel("X1 label")
plt.ylabel("Y1 label")
plt.title("Line Plot")


plt.subplot(1,3,2)           # subplot(rows, columns, position)
plt.scatter(x,y)
plt.xlabel("X2 label")
plt.ylabel("Y2 label")
plt.title("Scatter Plot")


plt.subplot(1,3,3)           # subplot(rows, columns, position)
plt.hist(x)
plt.xlabel("X3 label")
plt.ylabel("Y3 label")
plt.title("Histogram")

plt.show()