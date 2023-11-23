print("All about user input")
print("---------------------------------------------------------------------------")

username = input("Please enter your user name: ")
print(f"Congratulations! {username} You are logged in.")

_age = input("How old are you? : ")
print(_age)

age = int(_age)
print(age)

print(age == _age)

print("---------------------------------------------------------------------------")

active = True

while active:
    stringInput = input("Now, what are you thinking ? ")
    
    if(stringInput == 'exit'):
        active = False
    else:
        print(stringInput)
        

