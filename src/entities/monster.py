import json
from .abstract_entity import AbstractEntity , Stats

class Monster(AbstractEntity):
    def __init__(self, name, stats: Stats):
        super().__init__(name, stats)

class MonsterFactory:
    def __init__(self, json_path):
        with open(json_path, "r") as f:
            data = json.load(f)
        self.templates = data

    def create_monster(self, template_name = None):
        pass