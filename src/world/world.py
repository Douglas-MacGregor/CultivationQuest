from ..entities.monster import MonsterFactory
from ..entities.npc import NPCFactory
from .location import LocationFactory 
from ..entities.player import Player

class World:
    def __init__(self, location_factory, starting_location_name, monster_factory, npc_factory):
        self.year = 7
        self.day = 0
        self.location_factory = location_factory
        self.monster_factory = monster_factory
        self.npc_factory = npc_factory
        self.current_location = self.location_factory.create_location(starting_location_name, None)
