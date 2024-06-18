"""
Write the code to do the following:

- Create or connect to a database
- Create a table called Employees
- Insert data into the employees table
    id   name               salary
    101  Alice Johnson      55000
    102  Bob Smith          72000
    103  Charlie Brown      48000
    104  Diana Prince       60000
    105  Eve Adams          85000
- Select all records with a salary between 50000 and 75000
- Change Alice Johnson's salary to 58000
- Delete Bob Smith
- Change the salary of all employees with and id greater than 103 to 80000.
"""

# ******************************************************
# Import libraries
# ******************************************************

import sqlite3

# ==========  MAIN LOGIC - Database Manipulation with sqlite3  =============
try:
    # Open or create our sqlite database
    db = sqlite3.connect('employee_db')  # OR .connect('data/employee_db')

    # Get a cursor object to run queries.
    cursor = db.cursor()

    # Create a table called employees if it doesn't exist
    cursor.execute('''CREATE TABLE IF NOT EXISTS
                        employees(id INTEGER PRIMARY KEY,
                                  name TEXT NOT NULL,
                                  salary INTEGER)''')
    db.commit()

    # Insert data into table employees
    # Set the values in a list of tuples.
    employee_records = [(101, 'Alice Johnson', 55000),
                        (102, 'Bob Smith', 72000),
                        (103, 'Charlie Brown', 48000),
                        (104, 'Diana Prince', 60000),
                        (105, 'Eve Adams', 85000)]

    # ===== Insert new rows into the employees table.
    cursor.executemany('''INSERT OR REPLACE INTO employees(id, name, salary)
                          VALUES(?,?,?)''', employee_records)
    db.commit()

    # Display the table after creation and record inserts.
    cursor.execute('''SELECT * FROM employees''')
    print("\n**** Table after creation and record inserts ****\n")
    for row in cursor:
        print(f"Employee ID: {row[0]} Name: {row[1]} Salary: {row[2]}")

    # ===== Select all records with a salary between 50000 and 75000.
    cursor.execute('''SELECT * FROM employees
                      WHERE salary BETWEEN ? AND ?''', (50000, 75000))
    print("\n**** Records with a salary between 50000 and 75000 ****\n")
    for row in cursor:
        print(f"Employee ID: {row[0]} Name: {row[1]} Salary: {row[2]}")

    # ===== Change Alice Johnson’s salary to 58000.
    cursor.execute('''UPDATE employees SET salary = ?
                      WHERE name = ? ''', (58000, 'Alice Johnson'))
    db.commit()

    # Display update result for Alice Johnson.
    cursor.execute('''SELECT * FROM employees
                      WHERE name = ?''', ('Alice Johnson',))
    print("\n**** Updated record for Alice Johnson ****\n")
    for row in cursor:
        print(f"Employee ID: {row[0]} Name: {row[1]} Salary: {row[2]}")

    # ===== Delete Bob Smith’s row.
    cursor.execute('''DELETE FROM employees WHERE name = ? ''',
                   ('Bob Smith',))
    db.commit()

    # Display the table after deleting Bob Smith.
    cursor.execute('''SELECT * FROM employees''')
    print("\n**** Table after deleting Bob Smith ****\n")
    for row in cursor:
        print(f"Employee ID: {row[0]} Name: {row[1]} Salary: {row[2]}")

    # ===== Change the salary of all employees to 80000
    # where ids are greater than 103.
    cursor.execute('''UPDATE employees SET salary = ?
                      WHERE id > ? ''', (80000, 103))
    db.commit()

    # Display the table after updating salaries for IDs greater than 103.
    cursor.execute('''SELECT * FROM employees''')
    print("\n**** Salary changed to 80000 for IDs greater than 103 ****\n")
    for row in cursor:
        print(f"Employee ID: {row[0]} Name: {row[1]} Salary: {row[2]}")

except Exception as error_msg:
    # Roll back any changes if something goes wrong.
    db.rollback()
    raise error_msg
finally:
    # Close the database connection
    db.close()
