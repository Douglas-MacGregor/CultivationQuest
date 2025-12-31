from .abstract_entity import AbstractEntity , Stats
from ..systems.cultivation import CultivationStage, SpiritRoots, BodyConstitution, Qi
from .misc_entity import calculate_human_info

class Player(AbstractEntity):
    def __init__(self, name, stats : Stats):
        super().__init__(name, stats)

    def get_info(self):
        self.info = calculate_human_info(self.stats)

    def description(self):
        pass

    def interact(self):
        pass

    def attack(self, target):
        pass

    def defend(self, attacker):
        pass

    def cultivate(self, length):
        pass

    def charactersheet(self):
        return super().charactersheet()
    
    
class PlayerFactory:
    def __init__(self):
        pass

    def create_player(self, name):
        return Player(name)