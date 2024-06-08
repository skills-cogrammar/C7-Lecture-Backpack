from account import Account
from transaction import Transaction as Tran

account1 = Account("123456", 1000)
account2 = Account("123003", 1509)
account3 = Account("563003", 2509)

Tran.transfer(account1, account2, 300)

account1_bal = account1.get_balance()
account2_bal = account2.get_balance()

print("Account 1 balance: ", account1_bal)
print("Account 2 balance: ", account2_bal)