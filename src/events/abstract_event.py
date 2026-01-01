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

    def box_text(self, text: str, border_char: str = "#") -> str:
        """
        Takes a multiline string and returns it wrapped in a dynamically-sized box.
        Each line will have a left and right border character aligned.
        """
        lines = text.splitlines()

        # handle empty safely
        if not lines:
            return ""

        width = max(len(line) for line in lines)

        top_bottom = border_char * (width + 4)
        boxed = [top_bottom]

        for line in lines:
            boxed.append(f"{border_char} {line:<{width}} {border_char}")

        boxed.append(top_bottom)

        return "\n".join(boxed)