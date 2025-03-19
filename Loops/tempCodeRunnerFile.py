
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