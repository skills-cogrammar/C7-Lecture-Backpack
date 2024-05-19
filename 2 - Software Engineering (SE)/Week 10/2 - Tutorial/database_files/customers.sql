-- Creating the Customers Table
CREATE TABLE IF NOT EXISTS customers (
customer_id INTEGER PRIMARY KEY,
customer_name VARCHAR(50) NOT NULL,
customer_address VARCHAR(50) NOT NULL
);


INSERT INTO customers (customer_id, customer_name, customer_address) 
VALUES 
(100, 'John Doe', '123 Elm St, NY'),
(101, 'Jane Smith', '456 Oak St, LA'),
(102, 'Bob Johnson', '789 Pine St, TX'),
(103, 'Alice Brown', '171 Maple St, FL')
    ;

