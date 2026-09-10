import json

with open("Day-04-Exception-File-Handling/JSON/student.json","r") as file:
    student = json.load(file)

print(student)