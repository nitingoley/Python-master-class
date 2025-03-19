



my_dict = {
    "Name": "Nitin",
    "age": 21,
    "city": "Bareilly",
}


# print(my_dict) 


# operation in distionory    add new pair value

my_dic_op = {
    'Fruits': ["Banana", "Apple", "Orange"],
     'Category': "fruits"
}

# print(my_dic_op)

my_dic_op['Expense'] = 5000
# print(my_dic_op)


# update dict existing element 

my_dic_up = {
    'name': "Python",
    'version': 3.9
}

my_dic_up["version"] = 4.0
# print(my_dic_up)

# delete item in dict 

my_dic_del = {
    'name': "Low Level",
    "version" : 4.9,
     "Use_Case": ["Panic", "Anixety", "Depression"]
}

# print(my_dic_del)
del my_dic_del["Use_Case"]
# print(my_dic_del) 


#  Methods of Dictinory 

profile = {
    "name": "Harry",
    "age": 26,
    "salary": 430000
}

age = profile.get('age') 
# print(age) 

# keys = profile.keys()
# print(keys)

# items  = profile.items()
# print(items)


# popped = profile.pop('age', 'Not found')
# print(popped)

popped_i = profile.popitem()
# print(popped_i)
# print(profile)


# clear all elements 
# print(profile)

cleared = profile.clear()
# print(profile)


squares = {x: x*x*x for x in range(1,10)}
print(squares) 


# nested dict 

programming_language = {
    "python": {
        "name": "python" , "use_case": ['AI , ML , WebDev , DS']
    },
    "java":{ 
        "name": "java", "use_case": ['App Developement , Web Dev']
    },
    "javaScript": {
        "name": "javascript", "use_case": ['frontent dev, backend dev , Web Dev']
    }
}

# print(programming_language)


# Iterate the dict 

dic_lp = {
    "name": "Paras Gangwar",
     "age": 19,
      "city": "Bisal"
}

for k in dic_lp.items():
    print(k)