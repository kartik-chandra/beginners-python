print("Python for Beginners!")

#This section is about string

str = "This section is all about string"
print(str)

name = "Saurav"   #\n \t are use for new line and tab anf f is used at the start of a string to format string
print( f"Hi {name}, \nWelcome here")

#cases of string
mytest = "It is just a text to test all cases"
print("original: " + mytest.title())
print("title: " + mytest.title())
print("upper: " + mytest.upper())
print("lower: " + mytest.lower())

#strip will reduce spaces from string

text1 = " trip testing "
print ("[" + text1.strip() + "] - strip")
print ("[" + text1.rstrip() + "] - rstrip")
print ("[" + text1.lstrip() + "] - lstrip")

print("All about string")