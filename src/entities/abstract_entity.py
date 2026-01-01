
from abc import ABC, abstractmethod
from ..systems.cultivation import Qi, CultivationStage, SpiritRoots, BodyConstitution
from enum import Enum, auto

class Stats:
    def __init__(self, stats):
        self.qi = stats.get("qi", 0)
        self.health = stats.get("health", 10)
        self.qi_core_type = stats["qi core type"]
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
    def charactersheet(self, location):
        total = sum(self.stats.qi_aspects.values())
        top_five = sorted(self.stats.qi_aspects.items(), key=lambda x: x[1], reverse=True)[:5]
        info = (f"Name: {self.name}\n"
        f"Age: {self.stats.age['year']} years and {self.stats.age['day']} days\n"
        f"Location: {location.name}\n"
        f"Qi: {self.stats.qi}/{self.info['max qi']}  Health: {self.stats.health}/{self.info['max health']}\n"
        f"Mental State: {self.info['mind state']}\n"
        f"Cultivation Stage: {self.stats.cultivation_realm.value} (stage {self.stats.cultivation_stage})\n"
        f"Spirit Roots: {self.stats.spirit_roots.name.lower()}\n"
        f"Body Constitution: {self.stats.body_constitution.name.lower()}\n"
        f"Qi Aspects:\n"
        f"{top_five[0][0].value.title()}: {(top_five[0][1]/total)*100:.1f}%\n"
        f"{top_five[1][0].value.title()}: {(top_five[1][1]/total)*100:.1f}%\n" 
        f"{top_five[2][0].value.title()}: {(top_five[2][1]/total)*100:.1f}%\n"
        f"{top_five[3][0].value.title()}: {(top_five[3][1]/total)*100:.1f}%\n"
        f"{top_five[4][0].value.title()}: {(top_five[4][1]/total)*100:.1f}%\n"
        f"Qi Core Type: {self.stats.qi_core_type}\n")
        return info

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