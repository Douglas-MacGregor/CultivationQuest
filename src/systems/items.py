from enum import Enum, auto
from abc import ABC, abstractmethod

class ItemRarity(Enum):
    COMMON = auto()
    UNCOMMON = auto()
    RARE = auto()
    EPIC = auto()
    LEGENDARY = auto()
    MYTHIC = auto()

class ItemType(Enum):
    WEAPON = auto()
    ARMOR = auto()
    CONSUMABLE = auto()
    MATERIAL = auto()
    ACCESSORY = auto()

class Item(ABC):
    @abstractmethod
    def __init__(self, name):
        pass
    @abstractmethod
    def info(self):
        pass
    @abstractmethod
    def use(self, user):
        pass

class ItemFactory:
    def __init__(self, json_path):
        import json
        with open(json_path, "r") as f:
            data = json.load(f)
        self.templates = data["item_templates"]

    def create_item(self, template_name):
        pass