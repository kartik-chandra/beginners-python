class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def bark(self):
        print(f"GHAUUUU ... {self.name} is barking")
        
    def roll_over(self):
        print(f"{self.name} is roled over")
        
    def sit(self):
        print(f"{self.name} is sitting")
        
        
class AlsecialDog(Dog):
    charge_remains = 35
    
    def __init__(self, name, age):
        super().__init__(name, age)
        
    def Charge(self):
        print(f"{self.name} has {self.charge_remains}% charge left")
        
class CuteDog(Dog):
    charge_remains = 35
    
    def __init__(self, name, age):
        super().__init__(name, age)
        
    def bark(self):
        print(f"Chik Chik ... {self.name} is barking")
        
        
class Puppy():
    def __init__(self, name, age):
        self._name = name
        self.__age = age
        self.tag = "P001"
        
    def name(self):
        print(f"{self._name}")
        
    def growing(self):
        self.__age += 1
        self.__show()

    def __show(self):
        print(f"{self._name} is {self.__age} years old")
        
        

class Employee:        
    def __init__(self, id, name):
        self.id = id
        self.name = name
        
    def show(self):
        print(f"Id: {self.id}, Name: {self.name}")