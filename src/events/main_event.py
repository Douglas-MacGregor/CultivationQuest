from .abstract_event import Event
from ..game import Game

class MainLoopEvent(Event):
    def __init__(self, game):
        name = "Main Game Loop"
        description = self.box_text(game.player.charactersheet())
        description += "\n"
        description += "Choose an action to proceed."
        actions = ["Explore", "Meditate", "Train", "Travel" ,"View Full Character Sheet" ,"Save Game", "Quit"]
        super().__init__(name, description, actions)

    def trigger(self):
        return (self.name, self.description, self.actions)

    def resolve(self, action, game: Game):
        if action == "Explore":
            pass   #Implement exploration logic
        elif action == "Save Game":
            pass  #Implement save game logic
        elif action == "Meditate":
            pass
        elif action == "Train":
            pass
        elif action == "Travel":
            pass  
        elif action == "View Full Character Sheet":
            pass
        elif action == "Quit":
            game.ui.quit()

