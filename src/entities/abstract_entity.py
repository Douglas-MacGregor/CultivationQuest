
from abc import ABC, abstractmethod
from ..systems.cultivation import *
from enum import Enum, auto

class Stats:
    def __init__(self, stats):
        self.qi = stats["qi"]
        self.qi_type = stats["qi_type"]
        self.spirit = stats["spirit", 0]
        self.cultivation_level = stats.get("cultivation realm", 0)
        self.cultivation_stage = stats.get("cultivation stage", 0)
        self.spirit_roots = stats.get("spirit_roots", 0)
        self.body_constitution = stats.get("body_constitution", 2)

class AbstractEntity(ABC):
    @abstractmethod
    def __init__(self, name, stats: Stats):
        self.name = name
        self.stats = stats

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
    def stats(self):
        stats = {
            "qi": 0,
            "health": 0,
            "strength": 0,
            "agility": 0,
            "intelligence": 0,
            "spirit": 0
        }