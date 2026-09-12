import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y = [10,20,15,30,25]

plt.plot(x,y,label="Sales")


# Title to the Chart
plt.title("Sales Over Time")

# X-Axis, Y-Axis label
plt.xlabel("Months")
plt.ylabel("Sales")


# Adding a Grid
plt.grid()

# Adding legend
plt.legend()

plt.show()