from .abstract_event import Event
from .main_event import MainLoopEvent
from ..game import Game
from ..entities.misc_entity import create_human_mortal_basic_stats
from ..entities.player import Player
from ..systems.cultivation import BodyConstitution, SpiritRoots
from ..systems.backgrounds import Backgrounds

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
            game.player = Player(name = "New Player", stats=create_human_mortal_basic_stats())  # Placeholder for player creation
            game.create_world()
            game.world.current_location.enter(game.player, game)
            game.add_event(CharacterCreationEvent(game))
        elif action == "Load Game":
            game.add_event(LoadScreenEvent(game))
        elif action == "Quit":
            game.ui.quit()

class CharacterCreationEvent(Event):
    def __init__(self, game):
        name = "Character Creation"
        game.player.get_info()
        info = f"{game.player.charactersheet(location=game.world.current_location)}"
        description = self.box_text(info)
        description += "\n"
        description +="Create your character by selecting a name, improving attributes and choosing a background."
        actions = ["Select Name","Roll Character", "Back to Start Screen"]
        super().__init__(name, description, actions)

    def trigger(self):
        return (self.name, self.description, self.actions)

    def resolve(self, action, game):
        if action == "Select Name":
            game.add_event(NameEntryEvent(game))
        elif action == "Roll Character":
            game.player = Player(name="New Player", stats=create_human_mortal_basic_stats())
            game.player.get_info()
            game.add_event(CharacterCreationEvent(game))
        elif action == "Back to Start Screen":
            game.add_event(StartScreenEvent(game))
            game.player = None
            game.world = None
        

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
            game.add_event(StartScreenEvent(game))

class NameEntryEvent(Event):
    def __init__(self, game):
        name = "Name Entry"
        location = game.world.location_factory.create_location("starting village", world=game.world)
        game.player.get_info()
        description = self.box_text(game.player.charactersheet(location))
        description += "\n"
        description +="Please select your character's name:"
        actions = [
            "Wei Chen",
            "Li Na",
            "Zhang Wei",
            "Back to Start Screen"
        ]  # No predefined actions; user inputs name
        super().__init__(name, description, actions)

    def trigger(self):
        return (self.name, self.description, self.actions)

    def resolve(self, action, game: Game):
        if action == "Back to Start Screen":
            game.add_event(StartScreenEvent(game))
            game.player = None
            game.world = None
            return
        game.player.name = action  # Set the player's name to the input action
        if game.core.get("attribute upgrade points", 0) > 0:
            game.add_event(AttributeSelectionEvent(game))
        else:
            game.add_event(BackgroundSelectionEvent(game))

class AttributeSelectionEvent(Event):
    def __init__(self, game):
        name = "Attribute Selection"
        location = game.world.location_factory.create_location("starting village", world=game.world)
        game.player.get_info()
        description = self.box_text(game.player.charactersheet(location))
        description += "\n"
        description += f"You have {game.core.get("attribute upgrade points", 0)} attribute upgrade points to spend. Choose an attribute to upgrade:"
        actions = ["Body Constitution", "Cultivation Stage", "Spirit Roots"]
        super().__init__(name, description, actions)

    def trigger(self):
        return (self.name, self.description, self.actions)

    def resolve(self, action, game: Game):
        points = game.core.get("attribute upgrade points", 0)
        if points <= 0:
            game.add_event(BackgroundSelectionEvent(game))
            return

        if action == "Body Constitution":
            game.player.stats.body_constitution = BodyConstitution(min(game.player.stats.body_constitution.value + 1, BodyConstitution.TITANIC.value))
        elif action == "Cultivation Stage":
            if game.player.stats.cultivation_stage < 9:
                game.player.stats.cultivation_stage += 1
        elif action == "Spirit Roots":
            game.player.stats.spirit_roots = SpiritRoots(min(game.player.stats.spirit_roots.value + 1, SpiritRoots.DIVINE.value))

        game.core["attribute upgrade points"] = points - 1
        game.add_event(BackgroundSelectionEvent(game))

class BackgroundSelectionEvent(Event):
    def __init__(self, game):
        name = "Background Selection"
        location = game.world.location_factory.create_location("starting village", world=game.world)
        game.player.get_info()
        description = self.box_text(game.player.charactersheet(location))
        description += "\n"
        description += "Select a background for your character:"
        actions = game.core.get("backgrounds unlocked", ["riverside village", "island port"])
        actions.append("Back to Start Screen")
        super().__init__(name, description, actions)

    def trigger(self):
        return (self.name, self.description, self.actions)

    def resolve(self, action, game: Game):
        if action == "Back to Start Screen":
            game.add_event(StartScreenEvent(game))
            game.world = None
            game.player = None
            return
        game.create_world()
        Backgrounds[action.upper().replace(" ", "_")].value.apply_background_effects(game.player, game)
        game.add_event(MainLoopEvent(game))

