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
from dracykeiton.entity import Entity, mod_dep, data_node, properties
from dracykeiton.common import ActionPoint, Name, Wield
from .combat import Combat, Weapon, ConsumeAP1, ConsumeAP2
from ..skills import Skills

@mod_dep(ConsumeAP1)
class GunShoot(Entity):
    @unbound
    def check_action(self):
        return self.wielded and self.wielded.has_mod(Gun) and 0 < self.aim_range < 4

@mod_dep(Wield)
@data_node('get', 'accuracy', deps=['wielded'])
def SniperAccuracy(value, wielded):
    """Enchance accuracy if weapon has optical scope"""
    if not wielded or not wielded.has_mod(OpticalScope):
        return value
    else:
        return value ** (1.0/wielded.optical_scope)

@mod_dep(ConsumeAP2, SniperAccuracy)
class SniperShoot(Entity):
    @unbound
    def check_action(self):
        return self.wielded and self.wielded.has_mod(OpticalScope) and self.aim_range > 1

@mod_dep(Weapon)
class Gun(Entity):
    @unbound
    def _init(self):
        self.skill = 'guns'
        self.name = 'gun'
        self.base_damage = 2
        self.base_accuracy = 0.5

@properties({'optical_scope' : 1})
class OpticalScope(Entity):
    pass

@mod_dep(Gun, OpticalScope)
class SniperRifle(Entity):
    @unbound
    def _init(self):
        self.name = 'sniper rifle'
        self.base_damage = 10
        self.base_accuracy = 0.3
        self.optical_scope = 10
