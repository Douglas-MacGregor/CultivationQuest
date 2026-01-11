from ..entities.monster import MonsterFactory
from ..entities.npc import NPCFactory
from .location import LocationFactory 
from ..entities.player import Player

class World:
    def __init__(self, location_factory, monster_factory, npc_factory):
        self.location_factory = location_factory
        self.monster_factory = monster_factory
        self.npc_factory = npc_factory
        self.current_location = None
        self.world_event_queue = []
        

    def add_world_event(self, event):
        self.world_event_queue.append(event)
    
