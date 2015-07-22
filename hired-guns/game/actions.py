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
from mworld import *
import renpy.exports as renpy

test = True
can_do = True
conditions = dict()
actions = dict()
action = None
roll_result = list()

def roll_f(result):
    global roll_result
    roll_result = result
    for name in conditions:
        if conditions[name]():
            actions[name]()
            break
    else:
        raise Exception('no action has happened')

def roll(n):
    if test:
        return
    else:
        st = [None]
        renpy.call('roll_dices_action', n, roll_f)

def require_trait(trait, who='merc'):
    global can_do
    if test and can_do:
        if who == 'merc':
            can_do = selected_merc().has_trait(trait)
        else:
            can_do = all([m.has_trait(trait) for m in world.active_mission.mercs])

def outcome_condition(name, cond):
    conditions[name] = cond

def outcome_label(name, label):
    actions[name] = curry.curry(renpy.call)(label)

def get_dice(want, amount=1):
    try:
        want[0]
    except TypeError:
        want = (want, want)
    try:
        amount[0]
    except TypeError:
        amount = (amount, amount)
    def f():
        r = [dice for dice in roll_result if dice in range(want[0], want[1]+1)]
        return len(r) in range(amount[0], amount[1]+1)
    return f
