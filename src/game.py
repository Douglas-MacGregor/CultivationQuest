
from .world.world import World
from .entities.player import PlayerFactory

class Game:
    def __init__(self):
        self.world = None
        self.player = None

    def train(self):
        pass

    def explore(self):
        pass

    def fight(self):
        pass

    def get_status(self):
        pass

