from config import Config
from app.models import init_db
from app.services import fetch_paginated_api_data, find_new_ids
from logger import logger


def update():
    try:
        logger.info("Start fetch data operation")
        api_data = fetch_paginated_api_data()

        logger.info("Data Fetch operation finished. Identifying new IDs and storing")
        new_ids = find_new_ids(api_data)
        new_ids_number = len(new_ids)

        logger.info(f'{new_ids_number:n} new IDs identified. Storage successful')
    except Exception as e:
        logger.exception(f"An error occurred: {e}")

if __name__ == "__main__":
    init_db()
    update()


