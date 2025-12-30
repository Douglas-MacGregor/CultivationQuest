import json

class Monster:
    def __init__(self, name, level):
        self.name = name
        self.level = level

class MonsterFactory:
    def __init__(self, json_path):
        with open(json_path, "r") as f:
            data = json.load(f)
        self.templates = data["monster_templates"]

    def create_monster(self, template_name):
        pass