# #   function in Python  

# def add(a , b):
#     return a+b

# result = add(10,5)
# print(result)




# # types of  parameters 
# # Positional Paramters
# # default parameters
# #  Keyword (Named) Parameters  


# # Positional Paramters
# def greet(name, age):
#     print(f"Hello, my name is {name} and I am {age} years old.")

# greet("Alice" , 24)  # Correct way
# greet(28, "John")  # inCorrect way  


# # default parameters

# def greet1(name="Deepak"):
#     print(f"Hello , {name}") 

# greet1()
# greet1("Paras")



# #  Keyword (Named) Parameters  

# def greet3(name):
#     print(f"Hello Good Morning , {name}")

# greet3(name="Simmi")




# # locals and global variable in python 


# # Local and Global Variables in Python
# # In Python, variables have different scopes based on where they are defined. The two main types are local and global variables. 


# #  1. Local Variable
# # A local variable is declared inside a function.
# # It is accessible only within that function.
# # It does not affect variables outside the function.


# def localFunc():
#     message = "Hello, How are you"
#     print(message)

# localFunc()

# # 2. Global Variable
# # A global variable is declared outside any function.
# # It can be accessed inside and outside functions.
# # Functions can read global variables but cannot modify them directly unless specified.

# message= "Hi, This side from Global Varible"
# def globalFunc():
#     print(message)

# globalFunc()



# Decorator in function Python 

def my_decorator(func):
    def wrapper():
        print("Execute it before the code execution : )")
        func()
        print("Execute it after the code execution : )")
    return wrapper
@my_decorator
def say_Hello():
    print("Hello Good Evening")

say_Hello()

 

# Generator Function in Python 

def my_generator():
    yield 1
    yield 2
    yield 3

gen = my_generator() # create generator obj

# print(next(gen))
# print(next(gen))
# print(next(gen))


#  Example 1: Basic Lambda Function 

# add = lambda x, y : x*y for _ in range(2,100):