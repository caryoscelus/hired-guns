import renpy
from dracykeiton import random
from hiredguns.world import HiredGunsWorld

def random_merc(req_traits=()):
    """Get random merc from the team
    
    Optionally, filter only those having all req_traits
    """
    mercs = [merc for merc in HiredGunsWorld.instance().active_mission.mercs if merc.has_all_traits(req_traits)]
    if mercs:
        return random.choice(mercs)
    else:
        return None

def selected_merc():
    """Returns currently selected merc"""
    return HiredGunsWorld.instance().active_mission.selected

def affect_trait(trait, amount):
    """Affect trait on mission"""
    for merc in HiredGunsWorld.instance().active_mission.mercs:
        merc.affect_trait(trait, amount)

def get_team_skill(skill):
    return sum([merc.get_skill(skill) for merc in HiredGunsWorld.instance().active_mission.mercs])

def mission_outcome(status):
    """Call this when mission is over
    
    Right now, only calling mission_outcome('success') has effect.
    """
    if status == 'success':
        HiredGunsWorld.instance().pc.money += HiredGunsWorld.instance().active_mission.payment
    else:
        pass

def random_encounter(level=(0, float('inf')), with_tags=set(), without_tags=set()):
    try:
        level[0]
    except TypeError:
        level = (level, level)
    encounters = [
        encounter for encounter in HiredGunsWorld.instance().encounter_pool
            if  level[0] <= encounter.level <= level[1] and
                set(with_tags).issubset(encounter.tags) and
                set(without_tags).isdisjoint(encounter.tags)
    ]
    if encounters:
        return random.choice(encounters)()
    else:
        return None

def define_var(name, value=None):
    HiredGunsWorld.instance().active_mission.define_var(name)
    setattr(renpy.store, name, value)
