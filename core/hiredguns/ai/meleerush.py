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
from hiredguns.combat import FistHit, MeleeGrab, AimTarget

import math

class DoNothing(Entity):
    @unbound
    def act(self):
        return None

@mod_dep(
    ExamineFieldEntity,
    BattlefieldEntity,
    AimTarget,
)
class MeleeRush(Entity):
    @unbound
    def act(self):
        # TODO: read ap cost
        if not self.ap:
            return None
        if not self.aim_target or not self.aim_target.get():
            enemy = self.get_closest_enemy()
            self.aim_target = self.field.grid[enemy.xy()]
            if not self.aim_target:
                print('Cannot find any enemies')
                return None
        print('attack {}'.format(self.aim_target.get().name))
        distance = self.field.get_range(self.xy(), self.aim_target.xy())
        if distance > 1:
            print('approaching..')
            # TODO: pathfinding
            x, y = self.xy()
            dx, dy = [a-b for (a, b) in zip(self.aim_target.xy(), self.xy())]
            if abs(dx) > abs(dy):
                x += math.copysign(1, dx)
            else:
                y += math.copysign(1, dy)
            return self.move(x, y)
        elif distance == 1:
            print('grabbing..')
            self.plan_action_mod(MeleeGrab)
            return self.melee_action()
        else: # distance == 0
            print('hitting..')
            self.plan_action_mod(FistHit)
            return self.combat_action()
        return None
