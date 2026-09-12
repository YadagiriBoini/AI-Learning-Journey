import matplotlib.pyplot as plt

cities = ["Hyderabad", "Chennai", "Delhi"]
employees = [50, 35, 40]

plt.barh(cities, employees)
plt.xlabel("Employees")
plt.ylabel("Cities")
plt.title("Employees by City")

plt.show()