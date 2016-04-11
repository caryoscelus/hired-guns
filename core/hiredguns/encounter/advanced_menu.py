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

"""Hired-guns specific menu option"""

from .requirements import *
from .abstract_menu import AdvancedMenuOption, AdvancedMenuOutcome

from collections import OrderedDict

class HiredGunsAdvancedMenuOption(AdvancedMenuOption):
    def __init__(self, name):
        super(HiredGunsAdvancedMenuOption, self).__init__()
        self.name = name
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