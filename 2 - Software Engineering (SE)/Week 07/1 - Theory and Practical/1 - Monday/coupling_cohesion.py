# Low Coupling Code Example
class LowCouplingBank:
    def __init__(self, customer_database, account_manager):
        self.customer_database = customer_database
        self.account_manager = account_manager

    def open_account(self, customer):
        customer_id = self.customer_database.add_customer(customer)
        account_number = self.account_manager.create_account(customer_id)
        return account_number

# write use case

# High Coupling Code Example
class HighCoulingBank:
    def __init__(self):
        self.customer_database = CustomerDatabase()
        self.account_manager = AccountManager()

    def open_account(self, customer):
        customer_id = self.customer_database.add_customer(customer)
        account_number = self.account_manager.create_account(customer_id)
        return account_number
