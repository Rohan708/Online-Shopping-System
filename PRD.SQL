CREATE DATABASE PRD ;
USE PRD ;
CREATE TABLE products (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    brand VARCHAR(100),
    price DECIMAL(10, 2) NOT NULL,
    quantity INT NOT NULL,
    image_path VARCHAR(255) NOT NULL
);
 Select * from products;