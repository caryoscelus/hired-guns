##
##  Copyright (C) 2016 caryoscelus
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

"""Fighting with fists.."""

from dracykeiton.compat import *
from dracykeiton.entity import Entity, mod_dep, data_node, properties
from dracykeiton.common import Hurt, Accuracy, HitAction
from ..skills import Skills
from .combat import ConsumeAP1

@mod_dep(Skills, Hurt)
@data_node('get', 'hit_damage', priority='early')
def FistDamage(value):
    return 1

@mod_dep(Skills, Hurt)
@data_node('get', 'hit_damage', deps=['skills'])
def FistSKill(value, skills):
    return value * skills.get('unarmed_combat', 0)

@mod_dep(Skills, Accuracy)
@data_node('get', 'accuracy', deps=['skills'])
def FistAccuracy(value, skills):
    return value ** (1 / (skills.get('unarmed_combat', 0)+1))

@mod_dep(ConsumeAP1, HitAction, FistAccuracy, FistDamage, FistSKill)
class FistHit(Entity):
    @unbound
    def check_action(self):
        return self.wielded is None and self.aim_range == 0
