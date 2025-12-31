import json
from abc import ABC, abstractmethod
from enum import Enum, auto

class RegionType(Enum):
    VILLAGE = "village"
    TOWN = "town"
    CITY = "city"
    WILDS = "wilds"
    WILDERNESSES = "wildernesses"
    DEEP_WILDERNESSES = "deep_wildernesses"

class Location(ABC):
    @abstractmethod
    def __init__(self, name):
        self.name = name
        self.exploration_level = 0
        self.resources_concentration = 0

    @abstractmethod
    def description(self):
        pass

    @abstractmethod
    def enter(self, entity):
        pass

    @abstractmethod
    def connect(self, other_location):
        pass

    @abstractmethod
    def disconnect(self, other_location):
        pass

    @abstractmethod
    def entities(self):
        pass

    @abstractmethod
    def pass_time(self, time: int):
        pass




class LocationFactory:
    def __init__(self, json_path):
        with open(json_path, "r") as f:
            data = json.load(f)
        self.templates = data["location_templates"]

    def create_location(self, template_name, current_location : Location):
        pass