from abc import ABC, abstractmethod
from ..game import Game

class Event(ABC):
    @abstractmethod
    def __init__(self, name, description, actions):
        self.name = name
        self.description = description
        self.actions = actions

    @abstractmethod
    def trigger(self):
        return (self.name, self.description, self.actions)

    @abstractmethod
    def resolve(self, action, game : Game):
        pass