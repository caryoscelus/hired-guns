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
from collections import OrderedDict
import renpy.exports as renpy
import renpy.store as store

class AdvancedMenuOutcome(object):
    def __init__(self):
        self.condition = None
        self.label = None

class AdvancedMenuOption(object):
    def __init__(self, name):
        self.name = name
        self.traits = list()
        self.outcomes = OrderedDict()
    
    def psy_cost(self, n):
        self.psy = n
    
    def roll(self, n):
        self.roll_n = n
    
    def require_trait(self, trait):
        self.traits.append(trait)
    
    def outcome_condition(self, name, condition):
        if not name in self.outcomes:
            self.outcomes[name] = AdvancedMenuOutcome()
        self.outcomes[name].condition = condition
    
    def outcome_label(self, name, label):
        if not name in self.outcomes:
            self.outcomes[name] = AdvancedMenuOutcome()
        self.outcomes[name].label = label
    
    def can_do(self):
        return False
    
    def launch(self):
        renpy.call('roll_dices_action', self.roll_n, self.after_roll)
    
    def after_roll(self, result):
        for outcome in self.outcomes.values():
            if outcome.condition is None or outcome.condition(result):
                renpy.call(outcome.label)
                break

class AdvancedMenu(object):
    def __init__(self):
        self.caption = None
        self.options = list()
        self.active_option = None
    
    def __getattr__(self, name):
        return getattr(self.active_option, name)
    
    def start(self, caption):
        self.caption = caption
        self.options = list()
        self.active_option = None
    
    def option(self, name):
        self.active_option = AdvancedMenuOption(name)
        self.options.append(self.active_option)
    
    def launch(self):
        pass

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
    return curry.curry(get_dice_f)(want, amount)

def get_dice_f(want, amount, roll_result):
    r = [dice for dice in roll_result if want[0] <= dice <= want[1]]
    return amount[0] <= len(r) <= amount[1]
