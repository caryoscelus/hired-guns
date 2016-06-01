##
##  Copyright (C) 2016 caryoscelus
##
##  This file is part of HiredGuns
##  https://github.com/caryoscelus/hired-guns/
##  
##  This program is free software: you can redistribute it and/or modify
##  it under the terms of the GNU General Public License as published by
##  the Free Software Foundation, either version 3 of the License, or
##  (at your option) any later version.
##  
##  This program is distributed in the hope that it will be useful,
##  but WITHOUT ANY WARRANTY; without even the implied warranty of
##  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
##  GNU General Public License for more details.
##  
##  You should have received a copy of the GNU General Public License
##  along with this program.  If not, see <http://www.gnu.org/licenses/>.
##

"""Collection of util functions, previously located in mworld.py"""

from dracykeiton.compat import *
from dracykeiton import random
from dracykeiton.tb.turnman import Turnman
from hiredguns.combat import HGBattle
from hiredguns.world import HiredGunsWorld

def random_merc(req_traits=()):
    """Get random merc from the team
    
    Optionally, filter only those having all req_traits
    """
    pc = HiredGunsWorld.instance().pc
    mercs = [merc for merc in [pc]+pc.team if merc.has_all_traits(req_traits)]
    if mercs:
        return random.choice(mercs)
    else:
        print('WARNING: no random_merc selected')
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
        HiredGunsWorld.instance().active_mission.receive_payment(HiredGunsWorld.instance().pc)
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

def new_battle(*args, **kwargs):
    return HGBattle(Turnman, HiredGunsWorld.instance(), *args, **kwargs)
