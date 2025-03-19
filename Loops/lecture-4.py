# In Python there two types loops 

# 1- While loop 
# 2- for loop 


# while loop 
    #code execution 

i= 1
while i <= 5:
    print(i)
    i+=1



# for loop 

a = [1,2,3,4,5]
for i in a:
    print(a)


# Range function in python 
# range(start , stop , step) 

a = list(range(1,10,1))
print(a)


# Nested loop 

for i in range(1,3):
    for j in range(3,6):
        print(f'{i},{j}')


# break 

for num  in range(1,10,1):
    if num == 3:
        break
    print(num)



# Continue skip the interation 

for num in range(1,5,1):
    if num==3:
        continue
    print(num)


# pass statements for dummy statment 
