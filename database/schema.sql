DROP TABLE IF EXISTS products;
DROP TABLE IF EXISTS orders;

CREATE TABLE products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    price INTEGER NOT NULL,
    image TEXT NOT NULL,
    description TEXT NOT NULL,
    category TEXT NOT NULL
);

CREATE TABLE orders (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_name TEXT NOT NULL,
    phone TEXT NOT NULL,
    address TEXT NOT NULL,
    total INTEGER NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO products (name, price, image, description, category) VALUES
('Tahu Krispi Original',12000,'tahu1.jpg','Tahu krispi original yang renyah dan gurih.','New'),

('Tahu Krispi BBQ',15000,'tahu2.jpg','Tahu krispi dengan bumbu BBQ premium.','Regular'),

('Tahu Krispi Balado',15000,'tahu3.jpg','Perpaduan rasa balado pedas manis.','New'),

('Tahu Krispi Keju',17000,'tahu4.jpg','Tahu krispi dengan taburan keju premium.','Regular');