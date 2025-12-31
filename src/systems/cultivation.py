from enum import Enum, auto

class Qi(Enum):
    FIRE = "fire" # Represents fiery, intense energy
    WATER = "water" # Represents fluid, adaptable energy
    EARTH = "earth" # Represents stable, grounded energy
    WOOD = "wood" # Represents growth, vitality, and flexibility
    LIGHTNING = "lightning" # Represents sudden, powerful energy
    METAL = "metal" # Represents strength, resilience, and structure
    VOID = "void" # Represents spiritual, ethereal energy
    DEMONIC = "demonic" # Represents chaotic, dark energy
    CELESTIAL = "celestial" # Represents pure, divine energy
    SHADOW = "shadow" # Represents stealthy, elusive energy
    HEAVENLY = "healing" # Represents restorative, nurturing energy
    POISON = "poison" # Represents toxic, corrupting energy
    SPATIAL = "spatial" # Represents dimensional, space-bending energy
    TEMPORAL = "temporal" # Represents time-manipulating energy

class SpiritRoots(Enum):
    BLOCKED = auto()
    WEAK = auto()
    AVERAGE = auto()
    STRONG = auto()
    LEGENDARY = auto()
    PURE = auto() 

class BodyConstitution(Enum):
    FRAGILE = auto()
    WEAK = auto()
    AVERAGE = auto()
    STRONG = auto()
    IRON_WILLED = auto()
    TITANIC = auto()

class CultivationStage(Enum):
    MORTAL = "mortal"
    FOUNDATION_LAYING = "foundation laying"
    CORE_FORMATION = "core formation"
    NASCENT_SOUL = "nascent soul"
    MONARCH = "monarch"
    


