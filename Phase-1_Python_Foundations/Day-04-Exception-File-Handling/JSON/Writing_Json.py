import json

std1 = {
    "id": 999,
        "name": "Yada",
        "age": 20,
        "department": "CSE",
        "skills": [
            "Python",
            "HTML",
            "CSS"
        ],
        "marks": {
            "python": 55,
            "math": 77
        },
        "city": "Hyd",
        "active": True
}

with open("Day-04-Exception-File-Handling/JSON/student.json","w") as file:
    json.dump(std1,file,indent=4)