##
##  Copyright (C) 2015 caryoscelus
##
##  This file is part of HiredGuns
##  https://bitbucket.org/caryoscelus/hired-guns/
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

from dracykeiton.compat import *
from dracykeiton.util import curry
import mworld
from mworld import selected_merc, get_team_skill
import renpy.exports as renpy
from collections import OrderedDict
import actions

result = None

def start_action(name):
    global result
    result = dict({
        'can_do' : True,
        #'roll_n' : None,
        'actions' : list(),
        'branches' : OrderedDict(),
    })

def finish_action():
    pass

def roll(n):
    pass

def force_outcome(name, condition):
    pass

def require_trait(trait, who='merc'):
    if result['can_do']:
        if who == 'merc':
            result['can_do'] = selected_merc().has_trait(trait)
        else:
            result['can_do'] = all([m.has_trait(trait) for m in world.active_mission.mercs])

def require_skill(skill, level=1, who='merc'):
    if result['can_do']:
        if who == 'merc':
            result['can_do'] = selected_merc().has_skill(skill, level)
        elif who == 'team':
            result['can_do'] = all([m.has_skill(skill, level) for m in world.active_mission.mercs])
        elif who == 'sum':
            result['can_do'] = get_team_skill(skill) >= level
        else:
            raise ValueError('require_skill: "who" cannot be {}'.format(who))

def outcome_condition(name, cond):
    if not name in result['branches']:
        result['branches'][name] = list([lambda: True, None])
    result['branches'][name][0] = cond

def outcome_label(name, label):
    if not name in result['branches']:
        result['branches'][name] = list([lambda: True, None])
    result['branches'][name][1] = curry.curry(renpy.call)(label)

def get_dice(want, exactly=None, atleast=1, atmost=None):
    try:
        want[0]
    except TypeError:
        want = (want, want)
    
    if not exactly is None:
        try:
            amount = (exactly[0], exactly[1])
        except TypeError:
            amount = (exactly, exactly)
    elif not atmost is None:
        amount = (0, atmost)
    else:
        amount = (atleast, float('inf'))
    return curry.curry(actions.get_dice_f)(want, amount)

def affect_trait(trait, amount):
    result['actions'].append(curry.curry(mworld.affect_trait)(trait, amount))
