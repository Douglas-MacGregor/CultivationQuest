import json

class NPC:
    def __init__(self, name, role):
        self.name = name
        self.role = role

class NPCFactory:
    def __init__(self, json_path):
        with open(json_path, "r") as f:
            data = json.load(f)
        self.templates = data["npc_templates"]  

    def create_npc(self, template_name):
        pass