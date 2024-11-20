from flask import Flask, render_template
import requests
import sqlite3
from datetime import datetime
import json
import configparser
from random import randint
from time import sleep

app = Flask(__name__)
DB_FILE = 'db.sqlite'
<<<<<<< HEAD
API_URL = ''  # Replace with the actual API endpoint
TARGET_CATEGORY = 11
=======

config = configparser.ConfigParser()
config.read('config.ini')
API_URL = config['API']['API_URL']
<<<<<<< HEAD
TARGET_CATEGORY = config['API']['TARGET_CATEGORY']
>>>>>>> 7041a79 (Data Fetching and DB storage tested and working)
=======
WEBPAGE_TITLE = config['WEBPAGE']['TITLE']
>>>>>>> 6d49dd8 (Output page tested. Update page not created. Logic to launch data fetch to be removed)

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

# Fetch data from API
def fetch_api_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()  # Assumes the response is in JSON format
    else:
        print(f"Failed to fetch API data. Status code: {response.status_code}")
        return []

# Rotate through all pages in API
def fetch_paginated_api_data():
    all_responses = []
    iter = 1
    while True:
        response = fetch_api_data(API_URL + iter)
        if len(response) == 0:
            break

        all_responses.append(response)
        iter = iter + 1
        sleep(randint(1,5))
    
    return all_responses


def load_existing_products():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('SELECT id FROM products')
    existing_ids = {row[0] for row in cursor.fetchall()}
    conn.close()
    return existing_ids

def compare_downloaded_and_existing_products(existing_ids, downloaded_data, entries_datetime):
    new_entries = []
    
    for product in downloaded_data:  # Adjust key if needed
        product_id = product['id']
        if product_id not in existing_ids:
            product_name = product['title']['rendered']
            product_url = product['link']
            new_entries.append((product_id, entries_datetime, product_name, product_url))
            existing_ids.add(product_id)

    return new_entries

# Insert new entries into the database
def store_new_entries(new_entries):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    if new_entries:
        cursor.executemany('INSERT INTO products (id, identified_date, product, url) VALUES (?, ?, ?, ?)', new_entries)
    conn.commit()
    conn.close()

# Compare and update database
def find_new_ids(api_data):
    existing_ids = load_existing_products()
    
    entries_datetime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    new_entries = compare_downloaded_and_existing_products(existing_ids, api_data, entries_datetime)
    
    store_new_entries(new_entries)
    return new_entries

import json  # Add this import for handling JSON

# Fetch all entries from the database
def fetch_products():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('SELECT id, identified_date, product, url FROM products ORDER BY identified_date DESC LIMIT 100')
    products = [{"id": row[0], "identified_date": row[1], "product": row[2], "url": row[3]} for row in cursor.fetchall()]
    conn.close()
    
    return products

# Route to display new IDs
@app.route('/update')
def update():
    api_data = fetch_paginated_api_data()
    new_ids = find_new_ids(api_data)
    return render_template('update.html', new_ids=new_ids) #TODO

@app.route('/')
def index():
    products = fetch_products()
    return render_template('index.html', products=products, title=WEBPAGE_TITLE)

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
