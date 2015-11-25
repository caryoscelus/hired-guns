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
from dracykeiton.entity import Entity, mod_dep
from dracykeiton.action import action, category
from dracykeiton.common import ActionPoint, Name
from ..skills import Skills

@mod_dep(Skills, Combat, ActionPoint)
class GunCombat(Entity):
    @category('combat')
    @action
    def shoot(self, target, tool):
        self.perform_action(self, target, tool)
    
    @unbound
    def can_shoot(self, target, tool):
        if self.get_skill(tool.skill) < tool.level:
            return False
        return self.spend_ap(1)

@mod_dep(Weapon)
class Gun(Entity):
    @unbound
    def _init(self):
        self.skill = 'guns'
        self.name = 'gun'