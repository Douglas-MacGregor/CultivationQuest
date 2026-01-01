import json
from abc import ABC, abstractmethod
from enum import Enum, auto
from ..systems.cultivation import Qi

RESOURCE_REGENERATION_RATE = 0.01  # Base rate at which resources regenerate per time unit
QI_REGNERATION_RATE = 0.1  # Base rate at which Qi can be meditated per time unit
QI_LOSS_RATE = -0.05  # Base rate at which Qi depletes per time unit in harsh environments
EXPLORATION_RATE = 0.001  # Base rate at which exploration level increases per time unit

class RegionType(Enum):
    VILLAGE = "village"
    TOWN = "town"
    CITY = "city"
    WILDS = "wilds"
    WILDERNESSES = "wildernesses"
    DEEP_WILDERNESSES = "deep_wildernesses"

class Location(ABC):
    def __init__(self, name):
        self.name = name
        self.exploration_level = 0.0
        self.resources_concentration = 1.0
        self.connected_locations = []
        self.entities_present = []
        self.resources_present = []
        self.region_type = RegionType.WILDS
        self.description = ""
        self.qi_aspects = {
            Qi.FIRE: 0.0,
            Qi.WATER: 0.0,
            Qi.EARTH: 0.0,
            Qi.WOOD: 0.0,
            Qi.METAL: 0.0,
            Qi.WIND: 0.0,
            Qi.LIGHTNING: 0.0,
            Qi.VOID: 0.0,
            Qi.DEMONIC: 0.0,
            Qi.CELESTIAL: 0.0,
            Qi.SHADOW: 0.0,
            Qi.HEAVENLY: 0.0,
            Qi.POISON: 0.0,
            Qi.SPATIAL: 0.0,
            Qi.TEMPORAL: 0.0,
            Qi.NEAUTRAL: 0.0
        }
        self.qi_density = 0.01

    def enter(self, entity, game):
        if entity.is_player():
            # Only remove from current location if player is actually there and it's a different location
            if game.world.current_location and game.world.current_location != self and entity in game.world.current_location.entities_present:
                game.world.current_location.entities_present.remove(entity)
            game.world.current_location = self
        self.entities_present.append(entity)

    def connect(self, other_location):
        self.connected_locations.append(other_location)
        other_location.connected_locations.append(self)

    def disconnect(self, other_location):
        self.connected_locations.remove(other_location)
        other_location.connected_locations.remove(self)

    def entities(self):
        return self.entities_present

    def pass_time(self, time: int):
        self.resources_concentration += time * (1 - self.qi_density) * RESOURCE_REGENERATION_RATE
        self.resources_concentration = min(self.resources_concentration, 1.0)

    def meditate(self, entity, time: int):
        qi_gained = time * self.qi_density * QI_REGNERATION_RATE
        entity.stats.qi += qi_gained
        for qi_aspect in self.qi_aspects:
            entity.stats.qi_aspects[qi_aspect] += self.qi_density * QI_REGNERATION_RATE * time * self.qi_aspects[qi_aspect] if self.qi_aspects[qi_aspect] > 0 else QI_LOSS_RATE
        return qi_gained
    
    def explore(self, entity, time: int):
        exploration_gain = time * (EXPLORATION_RATE * self.qi_density)
        self.exploration_level += exploration_gain
        self.exploration_level = min(self.exploration_level, 1)
        if self.exploration_level >= 1.0:
            pass
        elif self.exploration_level >= 0.90:
            pass 
        elif self.exploration_level >= 0.8:
            pass
        elif self.exploration_level >= 0.7:
            pass
        elif self.exploration_level >= 0.6:
            pass
        elif self.exploration_level >= 0.5:
            pass
        elif self.exploration_level >= 0.4:
            pass
        elif self.exploration_level >= 0.3:
            pass
        elif self.exploration_level >= 0.2:
            pass
        elif self.exploration_level >= 0.1:
            pass
        return exploration_gain
    
    def add_monster(self, monsterFactory):
        pass

    def add_resource(self, resourceFactory):
        pass



class LocationFactory:
    def __init__(self, json_path):
        with open(json_path, "r") as f:
            data = json.load(f)
        self.templates = data

    def create_location(self, template_name, world=None):
        template = self.templates.get(template_name)
        if not template:
            raise ValueError(f"Location template '{template_name}' not found.")
        location = Location(template["name"])
        location.description = template.get("description", "")
        location.region_type = RegionType(template.get("region_type", "wilds"))
        for aspect in location.qi_aspects:
            location.qi_aspects[aspect] = template.get("qi_aspects", {}).get(aspect.value.lower(), 0.0)
        location.qi_density = template.get("qi_density", 0.01)
        return location
        