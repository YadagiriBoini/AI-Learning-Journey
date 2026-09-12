import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Name": ["Ravi", "Anand", "Raj", "Priya"],
    "Age": [22, 25, 21, 27],
    "Salary": [35000, 50000, 28000, 65000]
}

df = pd.DataFrame(data)

plt.bar(df["Name"], df["Salary"])
plt.xlabel("Employees")
plt.ylabel("Salary")
plt.title("Employees Salaries")

plt.savefig("Employees_Salaries.png")

plt.show()