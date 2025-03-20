
# 2️⃣ Parameterized Constructor 
class Car:
    def __init__(self, brand , model):
        self.brand = brand
        self.model = model


    def display(self):
        print(f"The Car name is {self.brand} and model {self.model}")


c1 = Car("Honda" , "Civic")
c2 = Car("maurti Sizuki", "Swift Dizer")

c1.display()
c2.display()


 

#  🔹 Types of Constructors in Python


# 3️⃣ Constructor with Default Values 

class People:
    def __init__(self , name="Unknown" , age=0):
        self.name = name
        self.age = age

    def show(self):
        print(f"Your name is {self.name} and your age {self.age}")

s1 = People() 
s2 = People("Udit", 77)

s1.show()
s2.show() 


# 1️⃣ Default Constructor (No Parameters) 


class Demo:
    def __init__(self):
        print("THis is the default constructor")

obj = Demo()