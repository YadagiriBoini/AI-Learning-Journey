
numbers = [10, 20, 30, 40, 50]

# Access Elements
print(numbers[2])
print(numbers[4])


# Useful Opertions
print("Initial List:",numbers)
numbers.append(60)
print("Appended List:",numbers)
numbers.remove(60)
print("Remove:",numbers)
numbers.pop()
print("Pop:",numbers)
print("Length of list:",len(numbers))
numbers.sort()
print("Sorted:",numbers)


# Slicing
print(numbers[1:4])


# Iterating thorugh list
for number in numbers:
    print(number)

for i in range(len(numbers)):
    print(numbers[i])