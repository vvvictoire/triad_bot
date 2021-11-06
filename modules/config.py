"""Handle configuration"""
import json


class Config():
    """Stores the configuration"""
    def __init__(self, config_filename) -> None:
        self.config = self.load_from_json(config_filename)

    def load_from_json(self, filename):
        """Load an object from a JSON file"""
        with open(filename, "r", encoding="utf-8") as file:
            data = json.load(file)
            return data
