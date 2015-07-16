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

"""Mercs trait and attitude system"""

from dracykeiton.compat import *
from dracykeiton.entity import Entity, mod_dep
from .nation import NATIONS

KNOWN_TRAITS = ('pacifist', 'brute') + NATIONS

class Traits(Entity):
    @unbound
    def _init(self):
        self.dynamic_property('traits', dict())
    
    @unbound
    def add_trait(self, trait, value=1.0):
        if not trait in KNOWN_TRAITS:
            print('WARNING: {} is not known trait!'.format(trait))
        self.traits[trait] = value
    
    @unbound
    def has_trait(self, trait):
        return self.traits.get(trait, 0) > 0
    
    @unbound
    def has_all_traits(self, traits):
        return all(self.has_trait(trait) for trait in traits)

class Attitude(Entity):
    """Contains attitude property; default is 0 (neutral)"""
    @unbound
    def _init(self, attitude=0):
        self.dynamic_property('attitude', attitude)

@mod_dep(Attitude, Traits)
class TraitAttitude(Entity):
    """Universal attitude changer based on traits."""
    @unbound
    def affect_trait(self, trait, amount):
        trait_value = self.traits.get(trait, 0)
        self.attitude += trait_value * amount
