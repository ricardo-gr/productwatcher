import configparser
from logger import here
import os

class Config:

    config_parser = configparser.ConfigParser()
    config_parser.read(os.path.join(here, 'config.ini'))

    try:
        API_URL = config_parser['API']['API_URL']
        WEBPAGE_TITLE = config_parser['WEBPAGE']['TITLE']
        SQLITE_PATH = config_parser['DB']['SQLITE_PATH']
    except configparser.noOptionError as e:
        raise ValueError(f"Missing required configuration option: {e}")
    except configparser.Error as e:
        raise ValueError(f"Error reading configuration file: {e}")
