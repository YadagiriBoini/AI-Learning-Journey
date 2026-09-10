
class Student:
    def __init__(self,name,age,branch):
        self.name = name
        self.age = age
        self.branch = branch


std1 = Student("Yadagiri",20,"AIML")
std2 = Student("Priya", 21, "ECE")

print(std1.name)
print(std1.age)
print(std1.branch)