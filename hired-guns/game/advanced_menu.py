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

from mworld import selected_merc, get_team_skill, affect_trait

import renpy.exports as renpy
import renpy.store as store

from collections import OrderedDict
from hiredguns.encounter.abstract_menu import AdvancedMenuOutcome, Requirement, AdvancedMenu
from hiredguns.encounter.requirements import *

class AdvancedMenuOption(object):
    def __init__(self, name):
        self.name = name
        self.requires = list()
        self.outcomes = OrderedDict()
        self.forced_conditions = OrderedDict()
        self.roll_n = None
    
    def psy_cost(self, n):
        self.requires.append(PsyCost(n))
    
    def money_cost(self, n):
        self.requires.append(MoneyCost(n))
    
    def affect_trait(self, trait, amount):
        self.requires.append(AffectTrait(trait, amount))
    
    def roll(self, n):
        self.roll_n = n
    
    def require_trait(self, trait, who='merc'):
        self.requires.append(RequireTrait(trait, who))
    
    def require_skill(self, skill, amount, who='merc'):
        self.requires.append(RequireSkill(skill, amount, who))
    
    def force_outcome(self, name, condition):
        self.forced_conditions[name] = condition
    
    def outcome_condition(self, name, condition):
        if not name in self.outcomes:
            self.outcomes[name] = AdvancedMenuOutcome()
        self.outcomes[name].condition = condition
    
    def outcome_label(self, name, label):
        if not name in self.outcomes:
            self.outcomes[name] = AdvancedMenuOutcome()
        self.outcomes[name].label = label
    
    def can_do(self):
        return all([req.check() for req in self.requires])
    
    def pay_costs(self):
        for req in self.requires:
            req.pay()
    
    def launch(self):
        self.pay_costs()
        
        for name in self.forced_conditions:
            cond = self.forced_conditions[name]
            if callable(cond):
                cond = cond()
            if cond:
                self.after_roll(forced=name)
        
        if self.roll_n != None:
            if callable(self.roll_n):
                self.roll_n = self.roll_n()
            renpy.call('roll_dices_action', self.roll_n, self.after_roll)
        else:
            self.after_roll()
    
    def after_roll(self, result=None, forced=None):
        if forced:
            renpy.call(self.outcomes[forced].label)
            return
        for outcome in self.outcomes.values():
            if outcome.condition is None or outcome.condition(result):
                renpy.call(outcome.label)
                break

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
