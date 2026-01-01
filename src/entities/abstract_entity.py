
from abc import ABC, abstractmethod
from ..systems.cultivation import Qi, CultivationStage, SpiritRoots, BodyConstitution
from enum import Enum, auto

class Stats:
    def __init__(self, stats):
        self.qi = stats.get("qi", 0)
        self.health = stats.get("health", 10)
        self.qi_type = stats["qi type"]
        self.spirit = stats.get("spirit", 0)
        self.cultivation_realm = stats.get("cultivation realm", CultivationStage.MORTAL)
        self.cultivation_stage = stats.get("cultivation stage", 0)
        self.spirit_roots = stats.get("spirit roots", SpiritRoots.AVERAGE)
        self.body_constitution = stats.get("body constitution", BodyConstitution.AVERAGE)
        self.age = stats.get("age", {"year": 18, "day": 1})
        self.race = stats.get("race", "human")
        self.background = stats.get("background", "not set")
        self.qi_aspects = stats.get("qi aspects", {
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
            Qi.NEAUTRAL: 1.0
        })

class AbstractEntity(ABC):
    @abstractmethod
    def __init__(self, name, stats: Stats):
        self.name = name
        self.stats = stats
        self.info = None
        self.is_player_flag = False

    @abstractmethod
    def charactersheet(self):
        sheet = f"Character Sheet:\n"
        sheet += f"Name: {self.name}\n"
        sheet += f"Race: {self.stats.race}\n"
        sheet += f"Background: {self.stats.background}\n"
        sheet += f"Qi Type: {self.stats.qi_type.value}\n"
        sheet += f"Cultivation Stage: {self.stats.cultivation_realm.value} (Stage {self.stats.cultivation_stage})\n"
        sheet += f"Spirit Roots: {self.stats.spirit_roots.name.lower()}\n"
        sheet += f"Body Constitution: {self.stats.body_constitution.name.lower()}\n"
        sheet += f"Age: {self.stats.age['year']} years and {self.stats.age['day']} days\n"
        sheet += f"Max Qi: {self.info['max qi']}\n"
        sheet += f"Current Qi: {self.stats.qi}\n"
        sheet += f"Max Health: {self.info['max health']}\n"
        sheet += f"Current Health: {self.stats.health}\n"
        sheet += f"Mind State: {self.info['mind state']}\n"
        return sheet

    @abstractmethod
    def description(self):
        pass

    @abstractmethod
    def interact(self):
        pass

    @abstractmethod
    def attack(self, target):
        pass

    @abstractmethod
    def defend(self, attacker):
        pass

    @abstractmethod
    def cultivate(self, length):
        pass

    @abstractmethod
    def get_info(self):
        pass

    @abstractmethod
    def is_player(self):
        return self.is_player_flag