
try:
    number = int(input("Enter a number: "))
except ValueError:
    print("Invalid input.")
finally:
    print("Program finished.")