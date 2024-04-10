import mysql.connector

# Connect to the mySQL server 
# Replace the username and password with your details
dataBase = mysql.connector.connect(
    host="localhost",
    user="root",
    password="CoGrammar123",
    database="examplePythonDatabase"
)

cursor = dataBase.cursor()

# Use the following to delete the table if you already ran the code
# clear = "DROP TABLE crew"
# cursor.execute(clear)

# You can store your queries in variables to make your code more readable
# Create the Table
createTable = """CREATE TABLE crew (crewID INT AUTO_INCREMENT PRIMARY KEY, 
firstName VARCHAR(255), lastName VARCHAR(255), roomNumber INT)"""
cursor.execute(createTable)

# Add entries to the table
insertInto = """INSERT INTO crew 
                (firstName, lastName, roomNumber) 
                VALUES (%s, %s, %s)"""
rows = [
    ("Zahra", "Mohamed", 7),
    ("Moumita", "Aich", 12)
]
cursor.executemany(insertInto, rows)
dataBase.commit()
print(cursor.rowcount, "rows were inserted.")

# Retrieve entries from the table
selectAll = "SELECT * FROM crew"
cursor.execute(selectAll)
result = cursor.fetchall()

for row in result:
    print(row)


selectCondition = """SELECT firstName FROM crew 
                    WHERE roomNumber = 7"""
cursor.execute(selectCondition)
result = cursor.fetchall()

for row in result:
    print(row)


# Update entries in the table
updateEntry = "UPDATE crew SET roomNumber = 6 WHERE firstName = 'Moumita'"
cursor.execute(updateEntry)
dataBase.commit()
print(cursor.rowcount, "row(s) were affected.")

# Delete entries from the table
deleteEntries = "DELETE FROM crew WHERE crewID = 2"
cursor.execute(deleteEntries)
dataBase.commit()
print(cursor.rowcount, "row(s) were deleted.")
