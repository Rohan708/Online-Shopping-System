CREATE DATABASE IF NOT EXISTS shopping_db;

USE shopping_db;

CREATE TABLE IF NOT EXISTS ODR (
    order_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_name VARCHAR(255) NOT NULL,
    customer_address TEXT NOT NULL,
    customer_phone VARCHAR(15) NOT NULL,
    customer_pincode VARCHAR(10) NOT NULL,
    product_name VARCHAR(255) NOT NULL,
    product_price DECIMAL(10, 2) NOT NULL,
    order_status VARCHAR(50) NOT NULL DEFAULT 'Processing',
    order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

Select * from ODR ;