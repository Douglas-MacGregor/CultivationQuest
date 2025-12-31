
from .world.world import World
from .entities.player import PlayerFactory, Player
from .world.location import LocationFactory
from .entities.monster import MonsterFactory
from .entities.npc import NPCFactory
from .ui.terminal_ui import TerminalUI


class Game:
    def __init__(self, ui):
        self.world = None
        self.player = None
        self.ui = ui
        self.events = []

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

    def start_new_game(player_name, location_json, monster_json, npc_json):
        pass

    def clear_events(self):
        self.events = []

    def add_event(self, event):
        self.events.append(event)

