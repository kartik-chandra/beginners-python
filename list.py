cars = ["Ford", "Toyota", "Corola", "BMW"]
print(cars)
print(cars[2])

cars.append("Aleon")
print(cars)

cars.insert(0, "Honda")
print(cars)
cars.insert(3, "Mahindra")
print(cars)

newCar = cars.pop()
print(newCar)
print(cars)

thirdCar = cars.pop(2)
print(thirdCar)
print(cars)

extraCar = "Honda"
cars.remove(extraCar)
print(cars)

cars.sort()
print(cars)

cars.sort(reverse = True)
print(cars)

newcars = sorted(cars)
print(newcars)
print(cars)

cars = ["Ford", "Toyota", "Corola", "BMW"]
print(cars)
print(cars[2])

cars.append("Aleon")
print(cars)

cars.insert(0, "Honda")
print(cars)
cars.insert(3, "Mahindra")
print(cars)

newCar = cars.pop()
print(newCar)
print(cars)

thirdCar = cars.pop(2)
print(thirdCar)
print(cars)

extraCar = "Honda"
cars.remove(extraCar)
print(cars)

cars.sort()
print(cars)

cars.sort(reverse = True)
print(cars)

newcars = sorted(cars)
print(newcars)
print(cars)

cars.reverse()
print(cars)

print(cars[-2])

print(f"Total number of cars: {len(cars)}")

#loop
for car in cars:
    print(car)

for i in range(1, 5):
    print(i)
    
even_numbers = list(range(2, 11, 2))
print(even_numbers)

squars = []
for val in range (2, 11, 2):
    squar = val ** 2
    squars.append(squar)

print(squars)
print(min(squars))
print(max(squars))
print(sum(squars))

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players)
print(players[0:3])
print(players[1:4])
print(players[2:])
print(players[-3:])



# Example List
my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Get elements from index 2 to 5 (not including 5)
sliced_list = my_list[2:5]
print(sliced_list)  # Output: [2, 3, 4]

# Get elements from the beginning to index 5 (not including 5)
sliced_list = my_list[:5]
print(sliced_list)  # Output: [0, 1, 2, 3, 4]

# Get elements from index 2 to the end
sliced_list = my_list[2:]
print(sliced_list)  # Output: [2, 3, 4, 5, 6, 7, 8, 9]

# Get the entire list (a copy of the original list)
sliced_list = my_list[:]
print(sliced_list)  # Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Using negative indices
sliced_list = my_list[-3:]  # Last three elements
print(sliced_list)  # Output: [7, 8, 9]

# Get every second element from index 1 to 7
sliced_list = my_list[1:8:2]
print(sliced_list)  # Output: [1, 3, 5, 7]

myFavourite = ["Mutton", "Hilsha", "Card"]
myFriendsFavourite = myFavourite[:]

myFavourite.append("Mango")

print(myFavourite)
print(myFriendsFavourite)


#Tupple
tuple1 = (1,"Saurav Biswas", "2500000", 4.6, "Google")
print(tuple1[1])
print(tuple1[3])

for item in tuple1:
    print(item)
    

thisYear = 2024

if (thisYear %2 == 0 or (thisYear % 400 == 0 and thisYear % 100 != 0)):
    print("It is a Leapyear")
    
