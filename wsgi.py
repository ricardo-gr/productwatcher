import sys
import os

sys.path.insert(0, '/var/www/tesoros/')

from logger import logger

logger.info(f"Version_info: {sys.version_info}")
logger.info(f"Venv: {sys.prefix}")

from app import create_app

application = create_app()
