class BankAccount:
    def __init__(self, account_number , balance):
        self.account_number = account_number  # its public attributes 
        self._bank_name = "Punjab National Bank"  # its protected attributes 
        self.__balance = balance  # private attributes 


    def deposit(self , amount):
        if amount > 0:
            self.__balance += amount
            print(f"₹{amount} deposited successfully!")
        else: 
            print("Invalid deposit amount!")


    # for Withdraw 

    def withdraw(self , amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"₹{amount} withdraw successfully!")
        else:
            print("Insufficent balance or invalid amount!")
        
    def get_balance(self):
        return self.__balance
    
# create an obj 
account = BankAccount("12345", 5000)

# protected attribute (accessible but should be avoided)
print(account.account_number)

# protected attribute (accessible but should be avoided)
print(account._bank_name)


# Private attribute (Cannot be accessed directly)
# print(account.__balance)  # This will raise an AttributeError



print(account.get_balance())


account.deposit(2000)


account.withdraw(1000)

print(account.get_balance())  