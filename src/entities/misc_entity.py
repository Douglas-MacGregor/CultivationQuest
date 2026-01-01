from .abstract_entity import AbstractEntity , Stats 
from ..systems.cultivation import CultivationStage, SpiritRoots, BodyConstitution, Qi , body_constitution_str_to_int , realm_str_to_int , spirit_float_to_string
from random import choice, gauss


def create_human_mortal_basic_stats():
    stats = Stats({
        "qi": choice([0,1,2]),
        "health": 10,
        "qi core type": "unformed",
        "spirit": 0,
        "cultivation realm": CultivationStage.MORTAL,
        "cultivation stage": choice([0, 1]),
        "spirit roots":choice([SpiritRoots.AVERAGE, SpiritRoots.WEAK]),
        "body constitution": choice([BodyConstitution.FRAGILE, BodyConstitution.WEAK, BodyConstitution.AVERAGE, BodyConstitution.STRONG]),
        "age": {"year": int(gauss(17,2)), "day": choice(range(1,365))},
        "background": "not set",
        "race": "human",
        "qi aspects": {
            Qi.FIRE: 0.0,
            Qi.WATER: 0.0,
            Qi.EARTH: 0.0,
            Qi.WOOD: 0.0,
            Qi.METAL: 0.0,
            Qi.WIND: 0.0,
            Qi.LIGHTNING: 0.0,
            Qi.VOID: 0.0,
            Qi.DEMONIC: 0.0,
            Qi.CELESTIAL: 0.0,
            Qi.SHADOW: 0.0,
            Qi.HEAVENLY: 0.0,
            Qi.POISON: 0.0,
            Qi.SPATIAL: 0.0,
            Qi.TEMPORAL: 0.0,
            Qi.NEAUTRAL: 1.0
        }
    })
    return stats

def calculate_human_info(stats: Stats):
    info = {
        "max qi": (4 + (stats.cultivation_stage * 2 ))  * max( realm_str_to_int(stats.cultivation_realm)+1, 1),
        "max health": 10 + ((stats.body_constitution.value) * 3) + ((stats.cultivation_stage + (realm_str_to_int(stats.cultivation_realm.value)*9)) * 2),
        "mind state": spirit_float_to_string(stats.spirit)
    }
    return info

