import psycopg2

## Bu değeri localinde çalışırken kendi passwordün yap. Ama kodu pushlarken 'postgres' olarak bırak.
password = 'hello'

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

def get_customer_who_bought_most_expensive_product():
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("""""")
    result = cur.fetchall()
    cur.close()
    conn.close()
    return result

# 2. Sipariş durumlarına göre açıklama
def get_order_status_descriptions():
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("""""")
    result = cur.fetchall()
    cur.close()
    conn.close()
    return result

# 3. Ortalama fiyatın üstündeki ürünler
def get_products_above_average_price():
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("""""")
    result = cur.fetchall()
    cur.close()
    conn.close()
    return result

# 4. Müşteri kategorileri
def get_customer_categories():
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("""""")
    result = cur.fetchall()
    cur.close()
    conn.close()
    return result

# 5. Son 30 gün içinde sipariş veren müşteriler
def get_recent_customers():
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("""""")
    result = cur.fetchall()
    cur.close()
    conn.close()
    return result

# 6. En çok sipariş verilen ürün
def get_most_ordered_product():
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("""""")
    result = cur.fetchall()
    cur.close()
    conn.close()
    return result

# 7. Ürün fiyatlarına göre etiketleme
def get_product_price_categories():
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("""""")
    result = cur.fetchall()
    cur.close()
    conn.close()
    return result