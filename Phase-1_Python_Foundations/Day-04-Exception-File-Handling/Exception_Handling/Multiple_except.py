
# Zero Division Error
try:
    number = int(input("Enter a number: "))
    res = 100/number
    print(res)
except ZeroDivisionError:
    print("You cannot divide by zero.")



# Value Error
try:
    number = int(input("Enter a number: "))
    print(number)
except ValueError:
    print("Please enter a valid number.")



# Index Error
numbers = [1,2,3,4,5]
try:
    print(numbers[6])
except IndexError:
    print("Index out of range")



# Key Error
student = {
    "name":"Yadagiri"
}
try:
    print(student["age"])
except KeyError:
    print("Key not found")



# Type Error
try:
    name = 10+"hello"
    print(name)
except TypeError:
    print("Can't assign str to int")