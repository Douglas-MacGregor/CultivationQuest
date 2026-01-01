
from .world.world import World
from .entities.player import PlayerFactory, Player
from .world.location import LocationFactory
from .entities.monster import MonsterFactory
from .entities.npc import NPCFactory
from .ui.terminal_ui import TerminalUI
import json


class Game:
    def __init__(self, ui):
        self.world = None
        self.player = None
        self.ui = ui
        self.events = []
        core_json_path = "src/core/progress.json"
        with open(core_json_path, "r") as f:
            self.core = json.load(f)
        

    def train(self):
        pass

    def explore(self):
        pass

    def fight(self):
        pass

    def get_status(self):
        pass

    def save(self, file_path):
        pass

    def load_game(self, file_path):
        pass

    def clear_events(self):
        self.events = []

    def add_event(self, event):
        self.events.append(event)

    def create_world(self):
        self.world = World(
            location_factory=LocationFactory("src/data/locations.json"),
            monster_factory=MonsterFactory("src/data/monsters.json"),
            npc_factory=NPCFactory("src/data/npcs.json")
        )
        self.world.current_location = self.world.location_factory.create_location("starting village", world=self.world)

