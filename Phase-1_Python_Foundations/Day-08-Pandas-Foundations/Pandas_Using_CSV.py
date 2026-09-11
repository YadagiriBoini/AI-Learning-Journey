import pandas as pd

# data = {
#     "Name": ["Ravi", "Anand", "Raj", "Priya"],
#     "Age": [20, 21, 19, 22],
#     "Marks": [85, 92, 76, 88]
# }
# df = pd.DataFrame(data)
# df.to_csv("Student_Data.csv", index=False)    # To create normal data to a csv file

df = pd.read_csv("Student_Data.csv")
print(df.head())

