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

parse_results = dict()
parse_result = None
roll_result = None

def start_action(name):
    global parse_result
    parse_result = parse_results[name]

def finish_action():
    pass

def roll_f(result):
    global roll_result
    roll_result = result
    
    for action in parse_result['actions']:
        action()
    
    for name in parse_result['branches']:
        if parse_result['branches'][name][0]():
            parse_result['branches'][name][1]()
            break
    else:
        raise Exception('no action has happened')

def roll(n):
    renpy.call('roll_dices_action', n, roll_f)

def require_trait(trait, who='merc'):
    pass

def outcome_condition(name, cond):
    pass

def outcome_label(name, label):
    pass

def get_dice(want, amount=1):
    pass

def get_dice_f(want, amount):
    r = [dice for dice in roll_result if dice in range(want[0], want[1]+1)]
    return len(r) in range(amount[0], amount[1]+1)

def affect_trait(trait, amount):
    pass
