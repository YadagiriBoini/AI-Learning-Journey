
import pandas as pd

data = {
    "Name": ["Ravi", "Anand", "Raj", "Priya"],
    "Age": [20, 21, 19, 22],
    "Marks": [85, 92, 76, 88]
}

df = pd.DataFrame(data)
df.index = ["a", "b", "c", "d"]

print( df.loc["b"] )   # Uses labels 

# iloc uses index/positions
