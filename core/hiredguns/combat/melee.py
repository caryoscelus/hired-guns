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
from dracykeiton.action import action, category
from dracykeiton.common import BattlefieldEntity, GridEntity

@mod_dep(BattlefieldEntity, GridEntity)
class MeleeGrab(Entity):
    @unbound
    def check_action(self):
        return self.aim_range == 1
    
    @category('combat')
    @action
    def melee_action(self):
        self.field.join_cells((self.x, self.y), (self.aim_target.x, self.aim_target.y))
    
    @unbound
    def can_melee_action(self):
        return self.spend_ap(2)

@mod_dep(BattlefieldEntity, GridEntity)
class MeleeFlee(Entity):
    @unbound
    def check_action(self):
        return self.aim_range == 0 and (self.x, self.y) != (self.aim_target.x, self.aim_target.y)
    
    @category('combat')
    @action
    def melee_action(self):
        self.field.unjoin_cells((self.x, self.y), (self.aim_target.x, self.aim_target.y))
    
    @unbound
    def can_melee_action(self):
        return self.spend_ap(2)
