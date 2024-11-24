import configparser

class Config:

    config_parser = configparser.ConfigParser()
    config_parser.read('config.ini')

    try:
        API_URL = config_parser['API']['API_URL']
        WEBPAGE_TITLE = config_parser['WEBPAGE']['TITLE']
    except configparser.noOptionError as e:
        raise ValueError(f"Missing required configuration option: {e}")
    except configparser.Error as e:
        raise ValueError(f"Error reading configuration file: {e}")