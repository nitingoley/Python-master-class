


# condtional statement 

""" 
if condition 
  statements
"""

age = int(input("Enter your afe = "))
if age > 18:
    print('You are eligible for vote !')


"""
if-else 

# if condition
#   statements
#   else
#   statements
# """

age = int(input("Enter your age ="))
if age > 18:
    print("You are man")
else:
    print("You are young boy!")




"""
eliff

"""

age = int(input("Enter your age ="))
if age > 18:
    print("You are man")
elif age<=0:
    print("Invalid age")
else:
    print("You are young boy!")

"""
In Python 3.10+ match and case were added.
"""

value = int(input("Enter a value: "))
match value:
    case 1:
        print("The value is 1!")
    case _ if value < 1:
        print("The value is less than 1.")
    case _ if value > 1:
        print("The value is greater than 1.")
