try:
    num = int(input("Enter a number: "))
    result = 10/num
except ZeroDivisionError:
    print("Cannot divide with zero")
except ValueError:
    print("Invalid input! Please enter a number")
except Exception as e:
    print("Some other error occurred:", e)
