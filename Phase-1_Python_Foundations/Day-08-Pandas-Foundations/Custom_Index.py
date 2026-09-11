import pandas as pd

marks = pd.Series(
    [85,92,77,56],
    index = ["Ravi","Joe","Sam","Raj"]
)

print(marks)

# Accessing using indexes
print( marks["Sam"] )