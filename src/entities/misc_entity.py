from .abstract_entity import AbstractEntity , Stats 
from ..systems.cultivation import CultivationStage, SpiritRoots, BodyConstitution, Qi
from random import choice, gauss

def create_human_mortal_basic_stats():
    stats = Stats({
        "qi": choice([0,1,2]),
        "health": 10,
        "qi type": choice([Qi.WIND, Qi.FIRE, Qi.WATER, Qi.EARTH, Qi.WOOD, Qi.METAL]),
        "spirit": 0,
        "cultivation realm": CultivationStage.MORTAL,
        "cultivation stage": choice([0, 1]),
        "spirit roots":choice([SpiritRoots.AVERAGE, SpiritRoots.WEAK, SpiritRoots.STRONG]),
        "body constitution": choice([BodyConstitution.FRAGILE, BodyConstitution.WEAK, BodyConstitution.AVERAGE, BodyConstitution.STRONG]),
        "age": {"year": int(gauss(17,2)), "day": choice(range(1,365))},
    })
    return stats

def calculate_human_info(stats: Stats):
    info = {
        "max qi": (4 + (stats.cultivation_stage * 2 ))  * max( realm_str_to_int(stats.cultivation_realm)+1, 1),
        "max health": 10 + (body_constitution_str_to_int(stats.body_constitution) * 3) + ((stats.cultivation_stage + (realm_str_to_int(stats.cultivation_realm.value)*9)) * 2),
        "mind state": spirit_float_to_string(stats.spirit)
    }
    return info

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