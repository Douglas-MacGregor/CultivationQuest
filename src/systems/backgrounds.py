from abc import ABC, abstractmethod
from enum import Enum, auto
from ..systems.cultivation import SpiritRoots , BodyConstitution
from ..systems.cultivation import Qi
from ..game import Game

class Background(ABC):
    @abstractmethod
    def __init__(self, name, description):
        self.name = name
        self.description = description

    @abstractmethod
    def apply_background_effects(self, entity, game):
        pass

class RiversideVillageBackground(Background):
    def __init__(self):
        super().__init__("riverside village", "A humble village by the river, known for its hardworking folk.")

    def apply_background_effects(self, entity, game):
        if entity.is_player():
            entity.stats.background = "riverside village"
            entity.stats.body_constitution = BodyConstitution(min(entity.stats.body_constitution.value + 1, BodyConstitution.ROBUST.value))
            entity.stats.spirit += 0.25
            entity.stats.qi_aspects[Qi.NEAUTRAL] -= 0.5
            entity.stats.qi_aspects[Qi.EARTH] += 0.25
            entity.stats.qi_aspects[Qi.WATER] += 0.25
            background_location = game.world.location_factory.create_location("riverside village", game.world)
            game.world.current_location = background_location
            game.world.current_location.enter(entity, game)
        else:
            entity.stats.background = "riverside village"
            entity.stats.body_constitution = BodyConstitution(min(entity.stats.body_constitution.value + 1, BodyConstitution.ROBUST.value))
            entity.stats.spirit += 0.25

class IslandPortBackground(Background):
    def __init__(self):
        super().__init__("island port", "A bustling island port, a hub of trade and adventure.")

    def apply_background_effects(self, entity, game : Game):
        if entity.is_player():
            entity.stats.background = "island port"
            entity.stats.spirit_roots = SpiritRoots(min(entity.stats.spirit_roots.value + 1, SpiritRoots.STRONG.value))
            entity.stats.spirit += 0.25
            entity.stats.qi_aspects[Qi.NEAUTRAL] -= 0.5
            entity.stats.qi_aspects[Qi.WIND] += 0.25
            entity.stats.qi_aspects[Qi.WATER] += 0.25
            background_location = game.world.location_factory.create_location("island port", game.world)
            game.world.current_location = background_location
            game.world.current_location.enter(entity, game)
        else:
            entity.stats.background = "island port"
            entity.stats.spirit_roots = SpiritRoots(min(entity.stats.spirit_roots.value + 1, SpiritRoots.STRONG.value))
            entity.stats.spirit += 0.25

class Backgrounds(Enum):
    RIVERSIDE_VILLAGE = RiversideVillageBackground()
    ISLAND_PORT = IslandPortBackground()