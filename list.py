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

cars.reverse()
print(cars)
