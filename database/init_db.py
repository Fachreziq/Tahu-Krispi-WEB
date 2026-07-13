import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATABASE = os.path.join(BASE_DIR, "database.db")


def init_db():
    conn = sqlite3.connect(DATABASE)
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
        image TEXT NOT NULL
    )
    """)

    # ==========================
    # TABEL ORDERS
    # ==========================
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS orders (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        customer_name TEXT NOT NULL,
        phone TEXT NOT NULL,
        address TEXT NOT NULL,
        total INTEGER NOT NULL
    )
    """)

    # ==========================
    # INSERT DATA PRODUK
    # ==========================
    cursor.execute("SELECT COUNT(*) FROM products")
    count = cursor.fetchone()[0]

    if count == 0:

        products = [

            (
                "Tahu Krispi Original",
                "Tahu krispi original yang renyah dan gurih.",
                12000,
                "tahu1.jpg"
            ),

            (
                "Tahu Krispi Pedas",
                "Tahu krispi dengan bumbu pedas.",
                15000,
                "tahu2.jpg"
            ),

            (
                "Tahu Krispi BBQ",
                "Tahu krispi rasa BBQ.",
                16000,
                "tahu3.jpg"
            ),

            (
                "Tahu Krispi Keju",
                "Tahu krispi taburan keju.",
                18000,
                "tahu4.jpg"
            )

        ]

        cursor.executemany("""
        INSERT INTO products
        (name, description, price, image)
        VALUES (?, ?, ?, ?)
        """, products)

    conn.commit()
    conn.close()

    print("===================================")
    print("Database berhasil dibuat.")
    print("Tabel products siap.")
    print("Tabel orders siap.")
    print("===================================")


if __name__ == "__main__":
    init_db()