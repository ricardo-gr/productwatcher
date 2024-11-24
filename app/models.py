import sqlite3
from datetime import datetime

DB_FILE = 'db.sqlite'

# Initialize SQLite database
def init_db():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY,
            identified_date TEXT,
            product TEXT,
            url TEXT
        )
    ''')
    conn.commit()
    conn.close()

def load_existing_product_ids():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('SELECT id FROM products')
    existing_ids = {row[0] for row in cursor.fetchall()}
    conn.close()
    return existing_ids

# Insert new entries into the database
def store_new_entries(new_entries):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    if new_entries:
        cursor.executemany('INSERT INTO products (id, identified_date, product, url) VALUES (?, ?, ?, ?)', new_entries)
    conn.commit()
    conn.close()

# Fetch all entries from the database
def load_product_listing():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('SELECT id, identified_date, product, url FROM products ORDER BY identified_date DESC, id DESC LIMIT 100')
    products = [{"id": row[0], "identified_date": row[1], "product": row[2], "url": row[3]} for row in cursor.fetchall()]
    conn.close()
    
    return products