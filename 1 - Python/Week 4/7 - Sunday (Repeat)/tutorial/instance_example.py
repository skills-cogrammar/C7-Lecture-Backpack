#Instance method
class BankAccount:
    def __init__(self,name,balance=0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        """
        The deposit and withdraw methods are instance methods
        because they operate on a specific bank account instance. 
        They have access to and can modify the instance specific
        attributes i.e. balance.
        """
        self.balance += amount 
        print(f"Deposited R{amount}. New balance: R{self.balance}") 

    def withdraw(self,amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew R{amount}. New balance: R{self.balance}")
        else:
            print("Insufficient funds") 

#Create an instance
account = BankAccount(name="Amare",balance = 1000)
account.deposit(200)
account.withdraw(500)