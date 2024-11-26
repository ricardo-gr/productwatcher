import requests
import json
from datetime import datetime
from .models import load_existing_product_ids, store_new_entries
from config import Config
from random import randint
from time import sleep
from logger import logger

# Fetch data from API
def fetch_api_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()  # Assumes the response is in JSON format
    else:
        logger.warning(f"Failed to fetch API data. Status code: {response.status_code}")
        return []

# Rotate through all pages in API
def fetch_paginated_api_data():
    all_responses = []
    iter = 1
    while True:
        logger.info(f"Fetching data from page {iter}")
        response = fetch_api_data(Config.API_URL + str(iter))
        if len(response) == 0:
            break

        logger.info(f"Data Fetch finished")
        all_responses.extend(response)
        iter = iter + 1
        sleep(randint(1,5))
    
    return all_responses

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

# Compare and update database
def find_new_ids(api_data):
    existing_ids = load_existing_product_ids()
    
    entries_datetime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    new_entries = compare_downloaded_and_existing_products(existing_ids, api_data, entries_datetime)
    
    store_new_entries(new_entries)
    return new_entries