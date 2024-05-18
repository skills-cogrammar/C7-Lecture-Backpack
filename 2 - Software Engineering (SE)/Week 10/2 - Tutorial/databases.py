import sqlite3

conn = sqlite3.connect('data\order_db.db')
conn.execute('PRAGMA foreign_keys = ON;')

cursor = conn.cursor()

# cursor.execute("Select * from Customers;")

# for customer in cursor:
#     print(customer[2])

# name = input("Please enter your name: ")

# cursor.execute("Select * from Customers where CustomerName = ?", (name,))

# print(cursor.fetchone())

name = "John Doe"

query = "Select Customers.CustomerName, Customers.CustomerAddress, "
query += "Orders.OrderID, Products.ProductID, Products.ProductName, Orders.quantity "
query += "from Customers "
query += "INNER JOIN Orders ON Customers.CustomerID = Orders.CustomerID "
query += "INNER JOIN Products ON Orders.ProductID = Products.ProductID "
query += "WHERE CustomerName = ?;"
cursor.execute(query, (name,))

for record in cursor:
    print(record)
