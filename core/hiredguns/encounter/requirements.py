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

"""Hired-guns specific Requirements"""

from dracykeiton.encounter.advanced_menu import Requirement

from ..world import HiredGunsWorld
from ..utils import selected_merc, get_team_skill

class RequireSkill(Requirement):
    api_name = 'require_skill'
    
    def __str__(self):
        return 'require {0.skill} {0.level} for {0.who}'.format(self)
    
    def __init__(self, skill, level, who='merc'):
        self.skill = skill
        self.level = level
        self.who = who
    
    def check(self):
        if self.who == 'merc':
            return selected_merc().has_skill(self.skill, self.level)
        elif self.who == 'team':
            return all([m.has_skill(self.skill, self.level) for m in active_mission().mercs])
        elif self.who == 'sum':
            return get_team_skill(self.skill) >= self.level
        else:
            raise ValueError('require_skill: "who" cannot be {}'.format(self.who))

class RequireTrait(Requirement):
    api_name = 'require_trait'
    
    def __str__(self):
        return 'require {0.trait} for {0.who}'.format(self)
    
    def __init__(self, trait, who='merc'):
        self.trait = trait
        self.who = who
    
    def check(self):
        if self.who == 'merc':
            return selected_merc().has_trait(self.trait)
        elif self.who == 'all':
            return all([m.has_trait(self.trait) for m in active_mission().mercs])
        elif self.who == 'any':
            return any([m.has_trait(self.trait) for m in active_mission().mercs])
        else:
            raise ValueError('require_skill: "who" cannot be {}'.format(self.who))

class MoneyCost(Requirement):
    api_name = 'money_cost'
    
    def __str__(self):
        return 'Costs {} moneys'.format(self.amount)
    
    def __init__(self, amount):
        self.amount = amount
    
    def check(self):
        return HiredGunsWorld.instance().pc.money > self.amount
    
    def pay(self):
        HiredGunsWorld.instance().pc.money -= self.amount

class PsyCost(Requirement):
    api_name = 'psy_cost'
    
    def __str__(self):
        return 'Costs {} psy'.format(self.amount)
    
    def __init__(self, amount):
        self.amount = amount
    
    def check(self):
        return selected_merc().psy > self.amount
    
    def pay(self):
        selected_merc().spend_psy(self.amount)

class AffectTrait(Requirement):
    api_name = 'affect_trait'
    
    def __str__(self):
        return 'Affects trait {} for {}'.format(self.trait, self.amount)
    
    def __init__(self, trait, amount):
        self.trait = trait
        self.amount = amount
    
    def check(self):
        return True
    
    def pay(self):
        affect_trait(self.trait, self.amount)
