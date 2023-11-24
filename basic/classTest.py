from Dog import Dog, AlsecialDog, Puppy, CuteDog, Employee

myDog = Dog("Royal", 2)
myDog.bark()
myDog.sit()

myAlsecialDog = AlsecialDog("Royal-A", 3)
myAlsecialDog.bark()
myAlsecialDog.Charge()

print(myAlsecialDog.charge_remains)

puppy = Puppy("Puppy", 1)
puppy.name()
puppy.growing()
print(puppy.tag)
print(puppy._name)


cuteDog = CuteDog("My Cute dog", 2)
cuteDog.bark()
cuteDog.sit()

employee2 = Employee(1, "Saurav Biswas")

employee2.show()