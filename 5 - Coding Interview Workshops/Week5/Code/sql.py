import mysql.connector

# Connect to the mySQL server 
# Replace the username and password with your details
dataBase = mysql.connector.connect(
    host="localhost",
    user="root",
    password="CoGrammar123"
)

# Create a new database on the server
cursor = dataBase.cursor()
cursor.execute("CREATE DATABASE examplePythonDatabase")

# To test the connection either reconnect:
# dataBase = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="CoGrammar123"
#     database="exampleDatabase"
# )

# Or look at the list of databases on the server 
cursor.execute("SHOW DATABASES")
for db in cursor:
   print(db)
