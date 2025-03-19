
# List is  
# Hetorgenous  
# ordered 
# mututable 


number1 = [1,2,3,4,5,6,6]
# print(type(number1))

# different ways to create a list 

number2 = list((1,3,4,5,7))
# print(type(number2))



# update element in list 

les = [1,2,3,5]
les[0] = 4
print(f"the updated list is: {les}") 


# update multipile elements togther 
les2 = [10,20,30,50]
print(les2)


# concate the list 
les3 = les + les2
print(les3)


# repeatation in list 

list1 = [1,2,3,"Hello" , True]
print(list1*4)


# memembership 

"""
in - True/False
not in - opposite
"""


les_1 = [1,3,4,5,6,7]

check = int(input('enter a number to check = '))
if check in les_1:
    print('Found!')
else:
    print("Not Found!")





les_2 = [6,7,8,9,10]
check = int(input("enter a number = "))

if check in les_2:
    print('Yes not found')
else:
    print("Found")


# alias   
# cloning in python 
list_1 = [1,2,3]
list_2 = list_1.copy()

list_2[0] = 100
print(list_1 , list_2)


# append element add in last position 


# sort the list ascending sort 
a= [100,809,32,1,3,50,2,-30,9]
a.sort()
# print(a)


# reverse the list 
a.reverse()
print(a)




# max and min in list 

maxList = [1,3,100,40,80]
print(max(maxList))
print(min(maxList))

# find the common elemements in list 

a1 = [1,2,4]
b1 = [3,2,5]


# convert it into set 

s1 = set(a1)
s2 = set(b1)

s3 = s1.intersection(s2)
print(list(s3))



# nested  list 

ns1 = [3,2,4]
ns2 = [5,56,67,a , [10,49,50]]

# print(ns2)


# list comprehsion 
squares = [i**2 for i in range(1,12) if i%2!= 0]
print(squares)



