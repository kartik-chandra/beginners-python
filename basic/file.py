# reading whole file
with open('./data/datafile.txt') as file_object:
    contents = file_object.read()
print(contents)

# reading all lines from a file
with open('./data/datafile.txt') as file_object:
    lines = file_object.readlines()
    
    for line in file_object:
        print(line)
print(lines)

#writing in a file
with open('./data/result.txt', 'a') as file_object:
    file_object.write("========== ONS ==========\n")


# fileText = "i am testing"
# fileName = input("Input your file name: ")

# with open('./data/' + fileName + ".txt", 'a') as file_object:
#     file_object.write(fileText)
    

