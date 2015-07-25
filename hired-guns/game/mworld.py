import renpy
from dracykeiton import random

def random_merc(req_traits=()):
    """Get random merc from the team
    
    Optionally, filter only those having all req_traits
    """
    mercs = [merc for merc in renpy.store.world.active_mission.mercs if merc.has_all_traits(req_traits)]
    if mercs:
        return random.choice(mercs)
    else:
        return None

def selected_merc():
    """Returns currently selected merc"""
    return renpy.store.world.active_mission.selected

def affect_trait(trait, amount):
    """Affect trait on mission"""
    for merc in renpy.store.world.active_mission.mercs:
        merc.affect_trait(trait, amount)

def mission_outcome(status):
    """Call this when mission is over
    
    Right now, only calling mission_outcome('success') has effect.
    """
    if status == 'success':
        renpy.store.world.pc.money += renpy.store.world.active_mission.payment
    else:
        pass
