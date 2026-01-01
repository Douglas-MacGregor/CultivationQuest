from enum import Enum, auto

class Qi(Enum):
    NEAUTRAL = "neutral" # Represents balanced energy
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
    WIND = "wind" # Represents swift, free-flowing energy

class SpiritRoots(Enum):
    BLOCKED = auto()
    WEAK = auto()
    AVERAGE = auto()
    STRONG = auto()
    PERFECT = auto()
    DIVINE = auto()

class BodyConstitution(Enum):
    FRAGILE = auto()
    WEAK = auto()
    AVERAGE = auto()
    STRONG = auto()
    ROBUST = auto()
    TITANIC = auto()

class CultivationStage(Enum):
    MORTAL = "mortal"
    FOUNDATION_LAYING = "foundation laying"
    CORE_FORMATION = "core formation"
    NASCENT_SOUL = "nascent soul"
    MONARCH = "monarch"

    
def realm_str_to_int(realm_str: str):
    mapping = {
        "mortal": 0,
        "foundation laying": 1,
        "core formation": 2,
        "nascent soul": 3,
        "monarch": 4
    }
    return mapping.get(realm_str, -1)

def spirit_float_to_string(spirit_float: float):
    if spirit_float < -0.75:
        return "corrupted"
    elif spirit_float < -0.50:
        return "tainted"
    elif spirit_float < -0.25:
        return "unbalanced"
    elif spirit_float < 0.25:
        return "neutral"
    elif spirit_float < 0.50:
        return "harmonious"
    elif spirit_float < 0.75:
        return "enlightened"
    else:
        return "transcendent"
    
def body_constitution_str_to_int(body_constitution: BodyConstitution):
    if body_constitution == BodyConstitution.FRAGILE:
        return 0
    elif body_constitution == BodyConstitution.WEAK:
        return 1
    elif body_constitution == BodyConstitution.AVERAGE:
        return 2
    elif body_constitution == BodyConstitution.STRONG:
        return 3
    elif body_constitution == BodyConstitution.ROBUST:
        return 4
    elif body_constitution == BodyConstitution.TITANIC:
        return 5
    else:
        # Default to AVERAGE if unknown constitution
        return 2
    
def sprit_roots_str_to_int(spirit_roots: SpiritRoots):
    if spirit_roots == SpiritRoots.BLOCKED:
        return 0
    elif spirit_roots == SpiritRoots.WEAK:
        return 1
    elif spirit_roots == SpiritRoots.AVERAGE:
        return 2
    elif spirit_roots == SpiritRoots.STRONG:
        return 3
    elif spirit_roots == SpiritRoots.PERFECT:
        return 4
    elif spirit_roots == SpiritRoots.TRANSENDENT:
        return 5
    else:
        # Default to AVERAGE if unknown spirit roots
        return 2

