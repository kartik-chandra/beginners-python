print("All about python dictionary")

dict01 = {"name": "Saurav", "Age" : 40, "Designation": "Senior Software Engineer"}
print(dict01)
print(dict01["Age"])

del dict01["Age"]
print(dict01)

#list in dictionary

dict02 = {
    "Id": 5,
    "Name":"Saurav Biswas",
    "Subject":["Data Structure & Algorithm", "Artificial Intelligency", "Computer Network", "Operation System", "Software Engineering"],
    "Grade": 3.54
}


subjects = dict02["Subject"]
print(subjects[1])
print(dict02["Subject"][2])


students ={ 
           "Student1": {
                "Id": 5,
                "Name":"Saurav Biswas",
                "Subject":["Data Structure & Algorithm", "Artificial Intelligency", "Computer Network", "Operation System", "Software Engineering"],
                "Grade": 3.54
            },
           "Student2": {
                "Id": 7,
                "Name":"Someone else",
                "Subject":["Artificial Intelligency", "Computer Network", "Operation System"],
                "Grade": 3.00
            },
}

print(students["Student1"]["Subject"][3])


for item in students["Student1"].items():
    print(item)

for key, value in students["Student1"].items():
    print(f"key: {key}, value: {value}")

print("-----------------------------------------------------------")

for key, value in students.items():
    for key1, value1 in value.items():
        print(f"key: {key1}, value: {value1}")

print("-----------------------------------------------------------")
