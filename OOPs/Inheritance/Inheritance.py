# Python supports the following types of inheritance:

# Single Inheritance
# Multiple Inheritance
# Multilevel Inheritance
# Hierarchical Inheritance
# Hybrid Inheritance


class Animal:
    def speak1(self):
        return "Animal sounds"
    

class Dog(Animal):
    def speak2(self):
        return "Woof ! woof!"

class Cat(Animal):
    def speak3(self):
        return "Meow Meow"
    

d = Dog()
c = Cat()
 

print(d.speak1())
print(d.speak2())
print(c.speak3())
print(c.speak1())