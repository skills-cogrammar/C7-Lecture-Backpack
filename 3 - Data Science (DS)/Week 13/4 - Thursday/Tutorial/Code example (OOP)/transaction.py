# facilitating transfers between accounts
from account import Account

class Transaction:
    def transfer(from_account, to_account, amount):
        if amount <= from_account.get_balance():
            from_account.withdraw(amount)
            to_account.deposit(amount)
            print("Transfer successful! :)")
        else:
            print("Transfer unsuccessful. Insufficient funds.")