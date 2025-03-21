# 2. Implementing Abstraction in Python
# Python provides the ABC (Abstract Base Class) module from abc to create abstract classes.

# 2.1. Abstract Class and Abstract Method
# Abstract Class: A class that cannot be instantiated and serves as a blueprint for other classes.
# Abstract Method: A method that has no implementation in the base class but must be implemented in derived classes.



from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):  # its  abstract method 
        pass

class Car(Vehicle):
    def start(self):
        return "Car engine started."
    

class Bike(Vehicle):
    def start(self):
        return "Bike engine Started."
    


car = Car()
bike = Bike()

print(car.start())
print(bike.start())