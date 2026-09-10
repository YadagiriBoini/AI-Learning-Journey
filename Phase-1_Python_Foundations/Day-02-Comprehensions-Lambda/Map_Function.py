
numbers = [1,2,3,4,5]

def sqaure(x):
    return x**2

result = map(sqaure, numbers)
print(list(result))





# Using lambda function
result1 = map(lambda x: x**2, numbers)
print(list(result1))