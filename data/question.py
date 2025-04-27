import psycopg2

def connect_db():
    return psycopg2.connect(
        host="localhost",
        port=5432,
        database="postgres",
        user="postgres",
        password="postgres"
    )

def create_view_completed_orders():
    with connect_db() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                CREATE OR REPLACE VIEW view_completed_orders AS
                SELECT * FROM Orders WHERE status = 'completed';
            """)
            conn.commit()

def create_view_electronics_products():
    with connect_db() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                CREATE OR REPLACE VIEW view_electronics_products AS
                SELECT * FROM Products WHERE category = 'Electronics';
            """)
            conn.commit()

def total_spending_per_customer():
    with connect_db() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                WITH customer_spending AS (
                    SELECT o.customer_id, SUM(p.price * o.quantity) AS total_spent
                    FROM Orders o
                    JOIN Products p ON o.product_id = p.product_id
                    WHERE o.status = 'completed'
                    GROUP BY o.customer_id
                )
                SELECT c.full_name, cs.total_spent
                FROM Customers c
                JOIN customer_spending cs ON c.customer_id = cs.customer_id;
            """)
            return cur.fetchall()

def order_details_with_total():
    with connect_db() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                WITH order_details AS (
                    SELECT o.order_id, p.product_name, (p.price * o.quantity) AS total_price
                    FROM Orders o
                    JOIN Products p ON o.product_id = p.product_id
                )
                SELECT * FROM order_details;
            """)
            return cur.fetchall()

def find_invalid_emails():
    with connect_db() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT * FROM Customers WHERE POSITION('@' IN email) = 0;
            """)
            return cur.fetchall()

def find_null_or_empty_emails():
    with connect_db() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT * FROM Customers WHERE email IS NULL OR email = '';
            """)
            return cur.fetchall()

def extract_lastname_from_fullname():
    with connect_db() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT full_name, 
                SUBSTRING(full_name FROM POSITION(' ' IN full_name) + 1) AS last_name
                FROM Customers;
            """)
            return cur.fetchall()

def concat_name_and_email():
    with connect_db() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT CONCAT(full_name, ' <', email, '>') AS contact_info FROM Customers;
            """)
            return cur.fetchall()

def cast_price_to_integer():
    with connect_db() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT product_name, CAST(price AS INTEGER) AS price_int FROM Products;
            """)
            return cur.fetchall()

def find_customers_not_example_email():
    with connect_db() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT * FROM Customers 
                WHERE COALESCE(STRPOS(email, 'example'), 0) = 0;
            """)
            return cur.fetchall()