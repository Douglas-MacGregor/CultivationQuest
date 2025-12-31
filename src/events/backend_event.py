from .abstract_event import Event
from ..game import Game
from ..entities.misc_entity import create_human_mortal_basic_stats
from ..entities.player import Player

class StartScreenEvent(Event):
    def __init__(self, game):
        name = "Start Screen"
        description = "The game is starting. Choose an option to proceed."
        actions = ["Start New Game", "Load Game", "Quit"]
        super().__init__(name, description, actions)

    def trigger(self):
        return (self.name, self.description, self.actions)

    def resolve(self, action, game: Game):
        if action == "Start New Game":
            game.add_event(CharacterCreationEvent(game))
        elif action == "Load Game":
            game.add_event(LoadScreenEvent(game))
        elif action == "Quit":
            game.ui.quit()

class CharacterCreationEvent(Event):
    def __init__(self, game):
        name = "Character Creation"
        game.player = Player(name = "New Player", stats=create_human_mortal_basic_stats())  # Placeholder for player creation
        game.player.get_info()
        description = f"{game.player.charactersheet()}\nCreate your character by entering a name and selecting attributes."
        actions = ["Enter Name", "Select Attributes", "Finish"]
        super().__init__(name, description, actions)

    def trigger(self):
        return (self.name, self.description, self.actions)

    def resolve(self, action, game):
        pass

class LoadScreenEvent(Event):
    def __init__(self, game):
        name = "Load Game"
        description = "Load a previously saved game."
        actions = ["Select Save File", "Back to Start Screen"]
        super().__init__(name, description, actions)

    def trigger(self):
        return (self.name, self.description, self.actions)

    def resolve(self, action, game : Game):
        if action == "Select Save File":
            pass  # Implement file selection logic
        elif action == "Back to Start Screen":
            game.add_event(StartScreenEvent())