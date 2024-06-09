'''
In basic terms, OOP is a programming pattern that is built around objects 
or entities, so it's called object-oriented programming.

In this file, we will create a banking system the procedural way 
i.e., without implementing any OOP principles.
'''

# defining a function called create account, returns dictionary with account details
def create_account(account_number, balance):
    return {"account_number": account_number, "balance": balance}

# retrieve account balance from dictionary
def get_balance(account):
    return account["balance"]

# deposit money, account balance increases
def deposit(account, amount):
    account["balance"] += amount

# withdraw means balance will decrease, must check if funds are sufficient
def withdraw(account, amount):
    if amount <= account["balance"]: 
        account["balance"] -= amount
    else:
        print("Insufficient funds.")

# use names to know which account is which, transfer funds between accounts
def transfer(from_account, to_account, amount):
    if amount <= from_account["balance"]:
        withdraw(from_account, amount)
        deposit(to_account, amount)
        print("Transfer successful!")
    else:
        print("Insufficient funds.")

# Using the functions defined above
account1 = create_account("123456", 1000)
print(account1)

account2 = create_account("654321", 500)
print(account2)

transfer(account1, account2, 300) #outputs whether or not it is successful

print("Account 1 balance:", get_balance(account1))
print("Account 2 balance:", get_balance(account2))

'''
Two main things we want to achieve here:
- representing a bank account & managing its balance
- facilitating transfers between accounts

These will be our key takeaways for implementing a divide and conquer approach for OOP.
'''
