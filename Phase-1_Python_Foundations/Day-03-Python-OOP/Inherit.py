
class Animal:
    def eat(self):
        return "Eating"

class Dog(Animal):
    def bark(self):
        return "Barking"


dog = Dog()
print(dog.eat())
print(dog.bark())