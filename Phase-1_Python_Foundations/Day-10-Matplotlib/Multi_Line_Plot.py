import matplotlib.pyplot as plt

months = [1, 2, 3, 4, 5]
sales = [10, 20, 15, 30, 25]
profit = [5, 10, 8, 15, 12]

plt.plot( months, sales, label="Sales")
plt.plot( months, profit, label="Profit")

plt.xlabel("Months")
plt.ylabel("Amount")
plt.title("Sales vs Profit")

plt.grid()

plt.legend()

plt.show()