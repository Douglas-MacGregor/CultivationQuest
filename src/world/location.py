import json

class Location:
    def __init__(self, name):
        self.name = name

class LocationFactory:
    def __init__(self, json_path):
        with open(json_path, "r") as f:
            data = json.load(f)
        self.templates = data["location_templates"]

    def create_location(self, template_name, current_location):
        pass