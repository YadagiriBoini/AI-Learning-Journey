
student = {
    "name":"Yadagiri",
    "Age":20,
    "Course":"CSE"
}

# Access Value:
print(student["name"])

# Change Value
student["Age"] = 21

# Add new value
student["College"] = "SVIT"

# Iterting through dict
for key,value in student.items():
    print(key,"-",value)

# Only keys
for key in student.keys():
    print(key)

# Only values
for value in student.values():
    print(value)