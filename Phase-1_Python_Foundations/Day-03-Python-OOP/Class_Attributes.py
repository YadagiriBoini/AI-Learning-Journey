
class Student:

    college = "SVIT"             # Shared by the class's objects unless overridden

    def __init__(self,name):
        self.name = name

std1 = Student("Yadagiri")
std2 = Student("Priya")

print(std1.name)
print(std1.college)

print()

print(std2.name)
print(std2.college)