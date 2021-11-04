"""Handle configuration"""
from modules import lib_triad_bot as ltb


class Config():
    """Stores the configuration"""
    def __init__(self, config_filename) -> None:
        self.config = ltb.load_from_json(config_filename)
