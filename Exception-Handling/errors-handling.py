# try:
#     x= 10/0 
# except ZeroDivisionError:
#     print("Cannot divide by zero!")




    # 2. Handling Multiple Exceptions 
    # try:
    #     num = int(input("Enter a number: "))
    # except ZeroDivisionError:
    #     print("You cannot divide by zero!")
    # except ValueError:
    #     print("Invalid input! please enter a number.") 


    # 3. Using else Block (Runs if no exception occurs) 

try: 
    x = 5/0
except ZeroDivisionError:
    print("Cannot divide with zero")
else:
    print("Division successful:", x) 


# 4. Using finally Block (Always Executes) 
try:
    file = open("test.txt" , "r")
    content = file.read()
except FileNotFoundError:
    print("FIle not found !")
finally: 
    print("Closing file operation")  


#  Basic Questions:
# What is exception handling in Python? Why is it important?

# Exception handling is a mechanism to handle runtime errors and prevent program crashes. It ensures smooth execution by catching errors and allowing the program to recover or handle them gracefully.
# Explain the difference between try-except, try-except-else, and try-except-finally.

# try-except: Catches exceptions and prevents the program from crashing.
# try-except-else: The else block runs only if no exception occurs.
# try-except-finally: The finally block always executes, whether an exception occurs or not.
# What happens if no exception occurs in the try block?

# If no exception occurs, Python skips the except block and executes the next statement after it. If there is an else block, it runs instead.
