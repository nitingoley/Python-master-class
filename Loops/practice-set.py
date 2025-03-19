#  print even numbers 



for num in range(1,20,1):
    if num % 2 == 0:
        print(num)
    else:
        print(num) 




# ask user to skip the value  

start = int(input('Enter start = '))
stop = int(input('Enter start = '))
if start > stop:
    print("Invalid number")
skip = int(input('number you want to skip the number'))


for i in range(start, stop):
    if i == skip:
        continue
    print(i)



# Multiplication Table 
num = int(input("Enter a number: "))
for i in range(1,11):
    print(f"{num} × {i} = {num * i}")