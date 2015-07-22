import renpy
from dracykeiton import random

def random_merc(req_traits=()):
    mercs = [merc for merc in renpy.store.world.active_mission.mercs if merc.has_all_traits(req_traits)]
    if mercs:
        return random.choice(mercs)
    else:
        return None

def selected_merc():
    return renpy.store.world.active_mission.selected

def affect_trait(trait, amount):
    for merc in renpy.store.world.active_mission.mercs:
        merc.affect_trait(trait, amount)
