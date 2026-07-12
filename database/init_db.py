import sqlite3
import os

BASE_DIR = os.path.dirname(__file__)
DB = os.path.join(BASE_DIR, "database.db")

conn = sqlite3.connect(DB)
cursor = conn.cursor()

# ==========================
# TABEL PRODUCTS
# ==========================
cursor.execute("""
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT,
    price INTEGER NOT NULL,
    image TEXT
)
""")

# ==========================
# TABEL ORDERS
# ==========================
cursor.execute("""
CREATE TABLE IF NOT EXISTS orders (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_name TEXT,
    phone TEXT,
    address TEXT,
    total INTEGER
)
""")

# ==========================
# DATA AWAL
# ==========================
cursor.execute("SELECT COUNT(*) FROM products")
count = cursor.fetchone()[0]

if count == 0:
    products = [
        (
            "Tahu Krispi Original",
            "Tahu original renyah.",
            12000,
            "tahu1.jpg"
        ),
        (
            "Tahu Krispi Pedas",
            "Tahu pedas.",
            15000,
            "tahu2.jpg"
        ),
        (
            "Tahu Krispi BBQ",
            "Rasa BBQ.",
            16000,
            "tahu3.jpg"
        ),
        (
            "Tahu Krispi Keju",
            "Rasa Keju.",
            18000,
            "tahu4.jpg"
        )
    ]

    cursor.executemany("""
    INSERT INTO products (name, description, price, image)
    VALUES (?, ?, ?, ?)
    """, products)

conn.commit()
conn.close()

print("Database berhasil dibuat.")