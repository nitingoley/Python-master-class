# Built-in Operator Polymorphism 

print(5+10)
print(32.3 + 3.1)
print("Hello" + "Yellow")
print([1, 2] + [3, 4]) 


# operator Overloading (Custom Polymorphism) 
# Python allows us to customize operators for user-defined objects using dunder (magic) methods.

# Operator	Overloaded Method
# + (Addition)	__add__(self, other)
# - (Subtraction)	__sub__(self, other)
# * (Multiplication)	__mul__(self, other)
# / (Division)	__truediv__(self, other)
# == (Equality)	__eq__(self, other) 


class Point:
    def __init__(self , x , y):
        self.x =x 
        self.y = y
    def __add__(self , other):
        return Point(self.x + other.x , self.y + other.y)
    
    def __str__(self):
        return f"({self.x}), {self.y}"
    
p1 = Point(10,20)
p2 = Point(20, 40) 

p3 = p1+p2 

print(p3)
        