
# Basic
squares = []
for i in range(1,6):
    squares.append(i**2)
print(squares)


# List Comprehension
square = [ i**2 for i in range(1,6)]
print(square)


# List Comprehension with conditions
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
even_number = [number for number in numbers if number%2==0]
print(even_number)


# Transforming Data
temperatures = [20, 25, 30, 35]
fahrenhit = [ (temp*9/5)+32 for temp in temperatures]
print(fahrenhit)


# Conditional Transforming
numbers = [1, 2, 3, 4, 5]
res = [ "Even" if num%2==0 else "Odd" for num in numbers ]
print(res)