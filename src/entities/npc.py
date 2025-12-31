import json
from .abstract_entity import AbstractEntity, Stats

class NPC(AbstractEntity):
    def __init__(self, name, stats: Stats):
        super().__init__(name, stats)

class NPCFactory:
    def __init__(self, json_path):
        with open(json_path, "r") as f:
            data = json.load(f)
        self.templates = data["npc_templates"]  

    def create_npc(self, template_name = None):
        pass