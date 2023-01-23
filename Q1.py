# Create animal base class with attribute and related methods 
# then create sub concrete subclass using animal eg of subclass: cow, horse, dog


class Animals:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass
    
    def move(self):
        return "I am moving"
    
    def eat(self):
        return "I am eating"
    
class Cow(Animals):
    def speak(self):
        return "Mooh!"
    
    def move(self):
        return super().move() + " and grazing"
    
    def eat(self):
        return super().eat() + " grass"

class Horse(Animals):
    def speak(self):
        return "Neigh!"
    
    def move(self):
        return super().move() + " and galloping"
    
    def eat(self):
        return super().eat() + " hay"

class Dog(Animals):
    def speak(self):
        return "Woof!"
    
    def move(self):
        return super().move()
    
    def eat(self):
        return super().eat()

cow = Cow("Lucy")
print(cow.name) 
print(cow.speak()) 
print(cow.move()) 
print(cow.eat()) 

print("\n")

horse = Horse("Chetak")
print(horse.name) 
print(horse.speak()) 
print(horse.move()) 
print(horse.eat()) 

print("\n")

dog = Dog("Tommie")
print(dog.name) 
print(dog.speak()) 
print(dog.move()) 
print(dog.eat()) 
