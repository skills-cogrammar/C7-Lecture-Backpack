-- Create a new database named 'MyShop'
CREATE DATABASE MyShop;

-- Create a table named 'Employees' with the following columns:
CREATE TABLE Employees (
  -- employee_id: unique identifier for each employee (integer, not null, auto-increments)
  employee_id int NOT NULL AUTO_INCREMENT,
  -- first_name: employee's first name (text, not null)
  first_name varchar(255) NOT NULL,
  -- last_name: employee's last name (text, not null)
  last_name varchar(255) NOT NULL,
  -- position_title: employee's job title (text, not null)
  position_title varchar(255) NOT NULL,
  -- PRIMARY KEY: constraint enforcing unique employee_id for each record
  PRIMARY KEY (employee_id)
);

-- Create a table named 'Products' with the following columns:
CREATE TABLE Products (
  -- product_id: unique identifier for each product (integer, not null, auto-increments)
  product_id int NOT NULL AUTO_INCREMENT,
  -- product_name: name of the product (text, not null)
  product_name int NOT NULL,  -- This line seems to have a typo, 'int' should likely be 'varchar(255)'
  -- PRIMARY KEY: constraint enforcing unique product_id for each record
  PRIMARY KEY (product_id)
);

-- Insert sample data into the 'Employees' table
INSERT INTO Employees (first_name, last_name, position_title)
VALUES ('John', 'Smith', 'Software Engineer'),
       ('Mary', 'Jones', 'Cashier'),
       ('Maria', 'Lisa', 'Cashier'),
       ('Ava', 'Bella', 'Managing Director'),
       ('David', 'Lee', 'Managing Executive');

-- Select all columns (*) from the 'Employees' table
select * from Employees;

-- Select all columns (*) from the 'Employees' table where position_title is 'Managing Director'
select * from Employees where position_title = 'Managing Director';

-- Select all columns (*) from the 'Employees' table where position_title contains '%Ma%' (case-insensitive)
select * from Employees where position_title like '%Ma%';
