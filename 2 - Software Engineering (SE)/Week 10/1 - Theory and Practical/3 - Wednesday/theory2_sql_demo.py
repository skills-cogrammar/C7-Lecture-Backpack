# Write the code to do the following tasks:
#
# - Create a table called employees.
# - Insert the following new rows into the employees table:

"""
  employ_num name     surname   department   position               level   salary 
    1001     Alice    Smith     HR           Manager                Senior  60000
    1002     Bob      Johnson   Engineering  Software Developer     Senior  75000
    1003     Charlie  Williams  Marketing    Marketing Coordinator  Mid     50000
    1004     David    Brown     Finance      Financial Analyst      Senior  65000
    1005     Emma     Jones     Sales        Sales Representative   Mid     55000
    1006     Frank    Miller    Engineering  Systems Engineer       Senior  80000
    1007     Grace    Davis     HR           HR Assistant           Junior  45000
    1008     Henry    Wilson    Finance      Accountant             Senior  70000
"""
# - Add a new employee: 1009,Isabella,Taylor,Marketing,Marketing Assistant,48000
# - Select all records with a salary between 45000 and 65000.
# - Change Emma Jones’ salary to 57000.
# - Delete Grace Davis' row.
# - Change the level to Junior for all people with a salary below 55000.

# ****************************************************** 
#   Import Libraries
# ******************************************************

import sqlite3

# ****************************************************** 
#   Declare Functions
# ****************************************************** 
def read_employee_data(file_name):
    """
    Read employee data from a file and return as a list of tuples.
    
    Args:
    file_name (str): The name of the input file containing employee data.
    
    Returns:
    list: A list of tuples, each tuple representing an employee record.
    """
    employees_data = []

    # Open and read the input file
    with open(file_name, "r") as file:
        # Iterate over each line in the file
        for line in file:
            # Split the line into fields using comma as delimiter
            fields = line.strip().split(',')
            # Convert employee number to integer
            employee_id = int(fields[0])
            # Extract other fields
            name = fields[1]
            surname = fields[2]
            department = fields[3]
            position = fields[4]
            level = fields[5]
            # Convert salary to float
            salary = float(fields[6])
            # Append the data to the employees_data list as a tuple
            employees_data.append((employee_id, name, surname, department, 
                                   position, level, salary))

    return employees_data

# ==========  MAIN LOGIC - Database Manipulation with sqlite3  =============
try:
    # Open or create a file that contains a sqlite3 database.
    # Be sure to create the folder before the time.  
    # <connect> only creates files and not folders.
    db = sqlite3.connect('employee_db')      # OR connect('data/employee_db')

    # Get a cursor object to run queries.
    # cursor is like an alias to prevent typing db.cursor() all the time 
    cursor = db.cursor() 

    # Test if this table exists else create a table called employees 
    # with id as the primary key and name must have a value (NOT NULL).

    cursor.execute('''CREATE TABLE IF NOT EXISTS employees (
                        employee_id INTEGER PRIMARY KEY, 
                        name TEXT NOT NULL, 
                        surname TEXT NOT NULL,
                        department TEXT NOT NULL,
                        position TEXT NOT NULL,
                        level TEXT NOT NULL,
                        salary REAL)''')
    db.commit()
    # NOTE: Tripple quotes allow for queries to run over multiple lines

    # ====== Set the values in a list/tuple.

    # Call the function to read employee data from the file
    employees_data_ = read_employee_data("employee_data.txt")
    # NOTE: the _ at the end of the list name. 
    # This is to indicate that we will use this list variable only one time.

    # ====== Insert new rows into the employees table. 
    # Replace duplicate key insertions.
    # Insert data into the table
    cursor.executemany('''INSERT OR REPLACE INTO employees (employee_id, name,
                            surname, department, position, level, salary)
                            VALUES (?, ?, ?, ?, ?, ?, ?)''', employees_data_)

    # ====== Inserting a single record 
    """
    # IF AUTOINCREMENT added to PRIMARY KEY table creation.
        cursor.execute('''CREATE TABLE IF NOT EXISTS employees (
                            employee_id INTEGER PRIMARY KEY AUTOINCREMENT, 
                            name TEXT NOT NULL, 
                            surname TEXT NOT NULL,
                            department TEXT NOT NULL,
                            position TEXT NOT NULL,
                            level TEXT NOT NULL,
                            salary REAL)''')

    # Define the values for the new row excluding the employee_id
    new_employee = ('Isabella', 'Taylor', 'Marketing', 'Marketing Assistant', 'Junior', 48000)

    # Execute the INSERT statement
    cursor.execute('''INSERT INTO employees (name, surname, department, 
                                            position, level, salary)
                    VALUES (?, ?, ?, ?, ?, ?)''', new_employee)
    """

    # Define the values for a new row
    new_employee = (1009, 'Isabella', 'Taylor', 'Marketing', 'Marketing Assistant', 
                    'Junior', 48000)

    # Execute the INSERT statement
    cursor.execute('''INSERT OR REPLACE INTO employees (employee_id, name, surname,
                        department, position, level, salary)
                        VALUES (?, ?, ?, ?, ?, ?, ?)''', new_employee)

    # Commit the change
    db.commit()

    # ====== Select all records in the table.
    cursor.execute('''SELECT * FROM employees''')

    # Display the rows in the select result.
    print()
    print("********* Table after creation and record inserts **********\n")
    # The records returned will be placed in a cursor object.
    for row in cursor:
        # Print each row in a two lines with labels using f-strings
        print(f"Employee Number: {row[0]}, Name: {row[1]}, Surname: {row[2]}")
        print(f"Department: {row[3]}, Position: {row[4]}, Level: {row[5]}, "
              f"Salary: {row[6]}\n")

    # The above is more efficient than using fetchall(), since with fetchall(),
    # all the rows will be loaded into memory. With - for row in cursor - the 
    # next row will overwrite the previous row and will limit the memory space used.
    
    # ====== Select all records with a salary between 45000 and 65000.
    cursor.execute('''SELECT * FROM employees 
                        WHERE salary BETWEEN ? AND ?''', (45000, 65000))
    # NOTE: In SQL the BETWEEN includes the lower and upper ranges.
    
    # Display the rows in the select result.
    print("********* Records with a salary between 45000 and 65000 **********\n")
    
    for row in cursor:
        # Print each row in a two lines with labels using f-strings
        print(f"Employee Number: {row[0]}, Name: {row[1]}, Surname: {row[2]}")
        print(f"Department: {row[3]}, Position: {row[4]}, Level: {row[5]}, "
              f"Salary: {row[6]}\n")

    # ====== Change Emma Jones’ salary to 57000.
    cursor.execute('''UPDATE employees SET salary = ? 
                   WHERE name = ? AND surname = ?''', (57000, 'Emma', 'Jones'))
    db.commit()

    # Display updated result for Emma Jones.
    cursor.execute('''SELECT * FROM employees 
                        WHERE name = ? AND surname = ?''', ('Emma', 'Jones'))

    # Though there is only 1 record here to display and the function fetchone() 
    # could have been used, I chose to use the -for row in cursor- option as to 
    # be consistent with the display format. 
    print("********* Updated record for Emma Jones **********\n")
    for row in cursor:
        # Print each row in a two lines with labels using f-strings
        print(f"Employee Number: {row[0]}, Name: {row[1]}, Surname: {row[2]}")
        print(f"Department: {row[3]}, Position: {row[4]}, Level: {row[5]}, "
              f"Salary: {row[6]}\n")

    """ This is how you would use the fetchone() function for the above.

    # Fetch the single record
    row = cursor.fetchone()

    # Display the record using f-strings
    print(f"Employee Number: {row[0]}, Name: {row[1]}, Surname: {row[2]}")
    print(f"Department: {row[3]}, Position: {row[4]}, Level: {row[5]}, "
            f"Salary: {row[6]}\n")
 
    """
    # ====== Delete Grace Davis' row.
    # Here we can either use name AND surname or we can use the employee_id

    # NOTE: A DELETE command will not give an error if the record does not exist.
    # If you need to know if the record exists, you will first have to do a 
    # SELECT and test that the cursor is not empty.

    # Execute the SELECT statement to check if records exist
    cursor.execute('''SELECT * FROM employees WHERE employee_id = ? ''', (1007,))

    # Check if the cursor is empty
    if not cursor.fetchall():
        print("No records found. No action taken.")
    else:
        # Execute the DELETE statement to delete records
        cursor.execute('''DELETE FROM employees WHERE employee_id = ? ''', (1007,))
        print("Records deleted successfully.")
        db.commit()

    # NOTE: A tuple with a single element needs to have 
    # a trailing comma to distinguish it from a parenthesised expression. 
    
    # Table after deleting Grace Davis.
    cursor.execute('''SELECT * FROM employees''')
    
    print("********* Table after deleting Grace Davis **********\n")
    for row in cursor:
        print(f"Employee Number: {row[0]}, Name: {row[1]}, Surname: {row[2]}")
        print(f"Department: {row[3]}, Position: {row[4]}, Level: {row[5]}, "
              f"Salary: {row[6]}\n")
    
    # ====== Change the level to Junior for all people with a salary below 55000.
    cursor.execute('''UPDATE employees SET level = ? 
                   WHERE salary < ? ''', ('Junior', 55000))
    db.commit()

    # Table after updating grade to 80 for all with id < 55.
    cursor.execute('''SELECT * FROM employees''')
    
    print("****** Level changed to Junior for salary less than 55000 *******\n")
    for row in cursor:
        print(f"Employee Number: {row[0]}, Name: {row[1]}, Surname: {row[2]}")
        print(f"Department: {row[3]}, Position: {row[4]}, Level: {row[5]}, "
              f"Salary: {row[6]}\n")

# Catch the exception
except Exception as error_msg:
    # Roll back any change if something goes wrong.
    db.rollback()
    raise error_msg

finally:
    # Close the db connection
    db.close()

# =================  END PROGRAM LOGIC HERE  ====================
"""
# ================= Additional functions and methods =============
# Use `fetchone` method to get a single tuple from the result
id = 1008

# Note the , in (id,) when only 1 ? in query
cursor.execute('''SELECT * FROM employees WHERE employee_id = ?''', (id,))
result = cursor.fetchone()

print(result)

# Use `fetchall` method to get all of the results that match our query.
cursor.execute('''SELECT name, surname, level FROM employees''')
results = cursor.fetchall()

print(results)

# Just like file handling, we can 
# use the `with` statement to handle the state of the db connection for us.

with sqlite3.connect('database.db') as db:   
    # Get a cursor object to run queries. 
    cursor = db.cursor() 
    cursor.execute('''SELECT * FROM table_name''')
    results = cursor.fetchall()
    print(results)

"""
    