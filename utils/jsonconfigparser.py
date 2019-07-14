import json

class JsonConfigParser:
    def __init__(self, filepath = "config.json"):
        self.config = self.__parse_json_config(filepath)

    def __parse_json_config(self, filepath):
        json_config = {}

        with open(filepath, "r") as config_file:
            json_config = json.load(config_file)

        return json_config