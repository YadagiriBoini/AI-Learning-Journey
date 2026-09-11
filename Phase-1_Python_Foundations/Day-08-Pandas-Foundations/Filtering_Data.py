
import pandas as pd

data = {
    "Name": ["Ravi", "Anand", "Raj", "Priya"],
    "Age": [20, 21, 19, 22],
    "Marks": [85, 92, 76, 88]
}

df = pd.DataFrame(data)

high_marks = df[df["Marks"]>85] 
print(high_marks)



print()



# Multiple Conditions
filtered = df[
    (df["Marks"]>85) &
    (df["Age"]>21)
]
print(filtered)