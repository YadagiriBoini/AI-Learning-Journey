import matplotlib.pyplot as plt

cities = ["Hyderabad", "Chennai", "Delhi"]
employees = [50, 35, 40]

plt.bar(cities,employees)

plt.xlabel("Cities")
plt.ylabel("Employees")
plt.title("Employees by City")

plt.show()