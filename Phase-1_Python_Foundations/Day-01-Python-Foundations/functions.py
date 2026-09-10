
def add(a,b):             # Basic function 
    return a+b


def greet(name):          # Parameters
    return "Hello "+name

def power(number, exponent=2): # Default Parameters
    return number**exponent


print(add(2,3))
print(greet("Yadagiri"))  # Arguments
print(power(5))
print(power(5,3))         # Override the Default Parameters