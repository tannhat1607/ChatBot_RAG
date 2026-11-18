

CREATE TABLE IF NOT EXISTS products (
    product_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    category VARCHAR(100),
    price DECIMAL(10, 2),
    status ENUM('active', 'inactive') DEFAULT 'active',
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        ON UPDATE CURRENT_TIMESTAMP
) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

INSERT INTO products (name, description, category, price, status)
VALUES
('iPhone 15', 'Apple iPhone 15 128GB', 'Điện thoại', 18990000.00, 'active'),
('Samsung Galaxy S24', 'Samsung Galaxy S24 256GB', 'Điện thoại', 20990000.00, 'active'),
('MacBook Air M2', 'Apple MacBook Air M2 13 inch', 'Laptop', 24990000.00, 'active'),
('Dell XPS 13', 'Dell XPS 13 Intel Core i7', 'Laptop', 32990000.00, 'active'),
('Logitech G Pro X', 'Chuột gaming Logitech G Pro X', 'Phụ kiện', 2990000.00, 'active'),
('AirPods Pro 2', 'Tai nghe Apple AirPods Pro thế hệ 2', 'Tai nghe', 5990000.00, 'active'),
('Sony WH-1000XM5', 'Tai nghe chống ồn Sony', 'Tai nghe', 8490000.00, 'active'),
('iPad Air M2', 'Apple iPad Air M2 11 inch', 'Máy tính bảng', 16990000.00, 'active'),
('ASUS ROG Strix', 'Laptop gaming ASUS ROG Strix', 'Laptop', 35990000.00, 'inactive'),
('Samsung Galaxy Tab S9', 'Máy tính bảng Samsung Galaxy Tab S9', 'Máy tính bảng', 19990000.00, 'active');