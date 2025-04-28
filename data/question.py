import psycopg2

## Bu değeri localinde çalışırken kendi passwordün yap. Ama kodu pushlarken 'postgres' olarak bırak.
password = 'postgres'

def connect_db():
    return psycopg2.connect(
        host="localhost",
        port=5432,
        database="postgres",
        user="postgres",
        password=password
    )

def create_view_completed_orders():
    with connect_db() as conn:
        with conn.cursor() as cur:
            cur.execute("""""")
            conn.commit()

def create_view_electronics_products():
    with connect_db() as conn:
        with conn.cursor() as cur:
            cur.execute("""""")
            conn.commit()

def total_spending_per_customer():
    with connect_db() as conn:
        with conn.cursor() as cur:
            cur.execute("""""")
            return cur.fetchall()

def order_details_with_total():
    with connect_db() as conn:
        with conn.cursor() as cur:
            cur.execute("""""")
            return cur.fetchall()

def find_invalid_emails():
    with connect_db() as conn:
        with conn.cursor() as cur:
            cur.execute("""""")
            return cur.fetchall()

def find_null_or_empty_emails():
    with connect_db() as conn:
        with conn.cursor() as cur:
            cur.execute("""""")
            return cur.fetchall()

def extract_lastname_from_fullname():
    with connect_db() as conn:
        with conn.cursor() as cur:
            cur.execute("""""")
            return cur.fetchall()

def concat_name_and_email():
    with connect_db() as conn:
        with conn.cursor() as cur:
            cur.execute("""""")
            return cur.fetchall()

def cast_price_to_integer():
    with connect_db() as conn:
        with conn.cursor() as cur:
            cur.execute("""""")
            return cur.fetchall()

def find_customers_not_example_email():
    with connect_db() as conn:
        with conn.cursor() as cur:
            cur.execute("""""")
            return cur.fetchall()