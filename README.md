# ProductWatcher

ProductWatcher is a Python project designed to monitor and track products from an external API, store the product data in a SQLite database, and display the tracked products on a web page using Flask.

## Installation

To install the required dependencies, run:
```bash
pip install -r 

requirements.txt


```

## Requirements

- Flask
- Requests

## Configuration

1. Create a `config.ini` file in the root directory with the following content:
    ```ini
    [API]
    API_URL = <your_api_url>

    [WEBPAGE]
    TITLE = Product Watcher

    [DB]
    SQLITE_PATH = db.sqlite
    ```

2. Ensure that the `db.sqlite` file is listed in the `.gitignore` to avoid committing it to the repository.

## Usage

1. Clone the repository:
    ```bash
    git clone https://github.com/ricardo-gr/productwatcher.git
    ```

2. Change into the project directory:
    ```bash
    cd productwatcher
    ```

3. Initialize the database and update product data:
    ```bash
    python updater.py
    ```

4. Run the Flask web application:
    ```bash
    python run.py
    ```

5. Access the web application by navigating to `http://127.0.0.1:5000/` in your web browser.

## Project Structure

- `app/`: Contains the main application code.
  - `__init__.py`: Initializes the Flask application.
  - `models.py`: Handles database operations.
  - `routes.py`: Defines the web routes.
  - `services.py`: Contains functions for fetching and processing API data.
  - `templates/`: Contains HTML templates for the web application.
    - `index.html`: Template for displaying the product listing.
- `config.ini`: Configuration file for API URL, webpage title, and SQLite database path.
- `config.py`: Loads configurations from `config.ini`.
- `db.sqlite`: SQLite database file (ignored by Git).
- `logger.py`: Configures logging for the application.
- `README.md`: Project documentation.
- `requirements.txt`: Lists the required Python packages.
- `run.py`: Entry point for running the Flask web application.
- `updater.log`: Log file for the updater script (ignored by Git).
- `updater.py`: Script for fetching and updating product data.
- `wsgi.py`: WSGI entry point for deploying the application.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## License

This project is licensed under the MIT License.
```