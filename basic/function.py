print("-------------------- FUNCTION --------------------")

#function greet_user()
def greet_user():
    print(f"greet_user(): It is from a function")
    
greet_user()

def full_Name(firstName, lastName = ''):
    if(lastName == ''):
        return f"{firstName}"
    else:
        return f"{firstName} {lastName}"
    
print(full_Name("Saurav"))
print(full_Name("Saurav", "Biswas"))

#keyword argument
print(full_Name(lastName = "Saurav", firstName = "Biswas"))

#list as a function parameter
def print_Names(names):
    for name in names:
        print(name)
        
print_Names(["Sachin", "Saurav", "Rahul"])

def courses(ids):
    allCourses = ["Bangla", "English", "Math", "Physics", "Chemistry", "Biology"]
    
    list1 = []
    
    for id in ids:
        if(len(allCourses) > id):
            list1.append(allCourses[id])
    return list1

print(courses([1, 3,9]))

def student_Details(name, crs):
    crss = ""
    for c in crs:
        crss += c + ", "

    return f"Name: {name}, Courses: {crss.rstrip(', ')}"   

#passing function as parameter
print(student_Details("Saurav", courses([1,3,5]))) 

print("-------------------- FUNCTION --------------------")
