import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = {
    "Name": ["Ravi", "Anand", "Raj", "Priya", "Kiran", "Arjun", "Sneha", "Vikram"],
    "Age": [20, 21, 22, 23, 24, 25, 26, 27],
    "Study_Hours": [2, 4, 3, 5, 6, 7, 5, 8],
    "Marks": [55, 65, 60, 72, 78, 85, 80, 92],
    "City": ["Hyderabad","Chennai","Delhi","Hyderabad","Chennai","Delhi","Hyderabad","Chennai"]
}

df = pd.DataFrame(data)

sns.kdeplot(
    data=df,
    x="Marks"
)

plt.show()