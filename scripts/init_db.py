import psycopg2

conn = psycopg2.connect(
    host="localhost",
    port=5432,
    database="postgres",
    user="postgres",
    password="postgres"
)
cur = conn.cursor()

cur.execute("""
CREATE TABLE Customers (
    customer_id SERIAL PRIMARY KEY,
    full_name VARCHAR(100),
    email VARCHAR(100),
    signup_date DATE
);
""")

cur.execute("""
CREATE TABLE Products (
    product_id SERIAL PRIMARY KEY,
    product_name VARCHAR(100),
    price NUMERIC(10,2),
    category VARCHAR(50)
);
""")

cur.execute("""
CREATE TABLE Orders (
    order_id SERIAL PRIMARY KEY,
    customer_id INT REFERENCES Customers(customer_id),
    product_id INT REFERENCES Products(product_id),
    order_date DATE,
    quantity INT,
    status VARCHAR(20) -- örneğin: completed, cancelled
);
""")

cur.execute("""
INSERT INTO Customers (full_name, email, signup_date) VALUES
('Ahmet Yılmaz', 'ahmet@example.com', '2022-01-15'),
('Ayşe Demir', 'ayse@example.com', '2022-05-22'),
('Mehmet Kaya', 'mehmet@example.com', '2022-07-30'),
('Fatma Şahin', 'fatma@example.com', '2022-09-18');
""")

cur.execute("""
INSERT INTO Products (product_name, price, category) VALUES
('Laptop', 15000.00, 'Electronics'),
('Smartphone', 8000.00, 'Electronics'),
('Coffee Machine', 1200.00, 'Home Appliances'),
('Book - SQL Basics', 150.00, 'Books');
""")

cur.execute("""
INSERT INTO Orders (customer_id, product_id, order_date, quantity, status) VALUES
(1, 1, '2023-02-10', 1, 'completed'),
(2, 2, '2023-03-12', 2, 'completed'),
(3, 4, '2023-04-05', 1, 'cancelled'),
(4, 3, '2023-05-20', 1, 'completed');
""")