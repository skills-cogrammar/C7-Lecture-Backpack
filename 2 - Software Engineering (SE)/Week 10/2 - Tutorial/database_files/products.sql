-- Creating the Products Table
CREATE TABLE IF NOT EXISTS products ( 
    product_id INTEGER PRIMARY KEY,
    product_name VARCHAR(255) NOT NULL,
    product_category VARCHAR(255) NOT NULL
);

INSERT INTO products (product_id, product_name, product_category) 
VALUES 
    (2001, 'Widget', 'Gadgets'),
    (2002, 'Thingamajig', 'Gadgets'),
    (2003, 'Doohickey', 'Tools'),
    (2004, 'Gizmo', 'Gadgets')
    ;

