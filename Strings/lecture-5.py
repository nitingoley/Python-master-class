
# string identification in string 

name1 = 'nitin1'

name2 = "nitin2"

name3 = '''Hello friends my name is 
  nitin goley and. I am from india  
  I loved building web application 
  and solved real world problem
'''
name4 = '''Hello friends my name is 
  ayush sharma and. I am from india  
  I loved building web application 
  and solved real world problem
'''


# things remember when working with strings 

# strings are immutable , indexed and iterable  


# print(name1, name2 , name3 , name4) 

# iterate string 

# for ans in name4:
#     print(name4)

# real world used strings 

# showing user information in web application like his name email or address  



# operation in strings 

name = "Nitin Goley"
# print(len(name1))

print(name[-2])

# slice in python 
# slice 
# slice[start:stop:stop] 

text = "python is my secondary programming langauge"
# print(text[::-1])


number = '10'
print(number * 20) 



# concate 
a = "nitin"
b =  "goley"

# print('Hell0', a + b)

# checking memebership 
text = 'user@gmail.com'

if "@" in text:
    print("Valid email")
else:
    print("Invalid Email")



# lower case  

# str = input("Enter your name").title()
# print(str) 


# find method 


str2 = "Searching"
print(str2.find("g"))