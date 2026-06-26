"""
Configuration Loader
"""

import json

def load_config():

    with open("src/config/config.json") as file:

        return json.load(file)
