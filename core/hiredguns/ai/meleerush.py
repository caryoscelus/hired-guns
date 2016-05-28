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

"""MeleeRush - monster AI that rushes in and attacks in melee"""

from dracykeiton.compat import *
from dracykeiton.entity import Entity, mod_dep
from dracykeiton.common import ExamineFieldEntity, BattlefieldEntity
from hiredguns.monster import Target

import math

class DoNothing(Entity):
    @unbound
    def act(self):
        return None

@mod_dep(
    ExamineFieldEntity,
    BattlefieldEntity,
    Target,
)
class MeleeRush(Entity):
    @unbound
    def act(self):
        if not self.target:
            self.target = self.get_closest_enemy()
            if not self.target:
                print('Cannot find any enemies')
                return None
        print('attack {}'.format(self.target.name))
        distance = self.field.get_range(self.xy(), self.target.xy())
        if distance > 1:
            # TODO: pathfinding
            x, y = self.xy()
            dx, dy = [a-b for (a, b) in zip(self.target.xy(), self.xy())]
            if abs(dx) > abs(dy):
                x += math.copysign(1, dx)
            else:
                y += math.copysign(1, dy)
            return self.move(x, y)
        return None
