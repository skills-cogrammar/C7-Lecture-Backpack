# representing a bank account & managing its balance

class Account:
    # properties: account_number, balance
    # methods: getting the balance, withdraw, deposit.

    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance
    
    def get_balance(self):
        return self.balance
    
    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("You have insufficient funds.")