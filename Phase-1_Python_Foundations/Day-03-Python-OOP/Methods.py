
class Student:
    def __init__(self,name,age,branch):
        self.name = name
        self.age = age
        self.branch = branch

    def Intro(self):
        return f"Hi! I am {self.name} a {self.age} years old student studying in {self.branch}"

std1 = Student("Yadagiri",20,"AIML")

print(std1.name)
print(std1.age)
print(std1.branch)
print(std1.Intro())