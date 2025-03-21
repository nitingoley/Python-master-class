#  Using with Statement (Best Practice)
# Using with automatically closes the file after execution. 

with open("read.txt", "r") as file:
    content = file.read()
    print(content)