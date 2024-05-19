-- Creating the Orders Table
CREATE TABLE IF NOT EXISTS orders (
    order_id INTEGER PRIMARY KEY,
    customer_id INT,
    product_id INT,
    quantity INT NOT NULL,
    order_date DATE NOT NULL,
    FOREIGN KEY (customer_id) REFERENCES customers (customer_id),
    FOREIGN KEY (product_id) REFERENCES products (product_id)
);

PRAGMA foreign_KEYS = 'ON';

-- iF NOT IN THEN BAD FOREIGN KEY RE;ATIONSHIPS WILL HAPPEN

INSERT INTO orders (customer_id, product_id, quantity, order_date) 
VALUES 
    (100, 2002, 10, 2024-05-25),
    (200, 2002, 10, 2024-05-25)
    ;

