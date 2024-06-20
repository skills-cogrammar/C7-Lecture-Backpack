CREATE DATABASE IF NOT EXISTS docker_practical;

USE docker_practical;

CREATE TABLE IF NOT EXISTS regular_customers (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100)
);

INSERT INTO regular_customers (name) VALUES ('Colonel Sanders'), ('Gopher'), ('Clippy');