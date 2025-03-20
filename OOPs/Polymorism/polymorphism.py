class Animal:
    def speak(self):
        return "Animal sound like"

class Dog(Animal):
    def speak(self):
        return "Woof! woof!"

class Cat(Animal):
    def speak(self):
        return "Meow ! Meow"
    
class Parrot(Animal):
    def speak(self):
        return "Crawf crawf"
    

d1 = Dog()
c1 = Cat()
p1 = Parrot()

print(d1.speak())
print(c1.speak())
print(p1.speak())