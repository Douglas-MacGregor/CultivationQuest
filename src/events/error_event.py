from .abstract_event import Event
from ..game import Game

class InvaildInputEvent(Event):
    def __init__(self, prior_event):
        self.prior_event = prior_event
        name = "Invalid Input"
        description = "The input provided is not valid. Please try again."
        actions = ["OK"]
        super().__init__(name, description, actions)
    
    def trigger(self):
        return (self.name, self.description, self.actions)
    
    def resolve(self, action, game : Game):
        game.events.insert(0, self.prior_event) # No specific action needed, just acknowledge the message