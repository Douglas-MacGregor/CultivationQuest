from abstract_entity import AbstractEntity , Stats

class Player(AbstractEntity):
    def __init__(self, name, stats: Stats):
        super().__init__(name, stats)
    
class PlayerFactory:
    def __init__(self):
        pass

    def create_player(self, name):
        return Player(name)