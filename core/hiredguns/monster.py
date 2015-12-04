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

"""Monster"""

from dracykeiton.compat import *
from dracykeiton.entity import Entity, mod_dep, simplenode, depends, listener
from dracykeiton.common import RoundingHp, Hp, Living, Name, Id, Description, ActionPoint, Movable, SimpleInventory, Wield
from .tactics import BattleTactic, TACTICS
from .combat import Combat, GunShoot, SniperShoot
from .skills import Skills

@mod_dep(Hp)
class DamageType(Entity):
    @unbound
    def _init(self):
        self.dynamic_property('damage_type_coeff', dict())
    
    @unbound
    def set_damage_type_coeff(self, dtype, coeff):
        self.damage_type_coeff[dtype] = coeff
    
    @unbound
    def receive_damage(self, amount, dtype='default'):
        self.hurt(amount*self.damage_type_coeff.get(dtype, 1.0))

class Target(Entity):
    """Target in battle"""
    @unbound
    def _init(self):
        self.dynamic_property('target', None)

class Tactics(Entity):
    """Contains basic tactic direction."""
    @unbound
    def _init(self):
        self.dynamic_property('tactic', BattleTactic('default'))
    
    @unbound
    def _load(self):
        self.add_set_node('tactic', self.check_tactic())
    
    @simplenode
    def check_tactic(value):
        if value is None or value.name in TACTICS:
            return value
        raise ValueError('there is no such tactic as {}'.format(value))

@mod_dep(Living)
class PsyPoints(Entity):
    @unbound
    def _init(self):
        self.dynamic_property('psy', 0)
        self.dynamic_property('maxpsy', 0)
    
    @unbound
    def _load(self):
        self.add_set_node('psy', self.psy_cap())
        self.add_listener_node('living', self.restore_psy_if_born())
    
    @unbound
    def spend_psy(self, amount):
        if amount <= self.psy:
            self.psy -= amount
            return True
        return False
    
    @unbound
    def full_psy(self):
        self.psy = self.maxpsy
    
    @depends('maxpsy')
    @simplenode
    def psy_cap(value, maxpsy):
        return min(value, maxpsy)
    
    @listener
    def restore_psy_if_born(self, target, value):
        if value == 'alive':
            self.full_psy()

@mod_dep(Movable)
class AdjacentMovable(Entity):
    @unbound
    def _init(self):
        self.add_move_constraint(self.adjacent_can_move)
    
    @unbound
    def adjacent_can_move(self, x, y):
        if abs(x-self.x)+abs(y-self.y) > 1:
            return False
        return True

@mod_dep(
    # base attributes
    RoundingHp,
    DamageType,
    PsyPoints,
    SimpleInventory,
    # combat
    Tactics,
    Target,
    ActionPoint,
    AdjacentMovable,
    Skills,
    Combat,
    # misc
    Name,
    Id,
    Description,
)
class Monster(Entity):
    """Base class for entities in battle (including mercs)"""
    @unbound
    def _init(self, name='monster'):
        self.name = name
        self.maxhp = 1
        self.maxap = 1
        self.known_actions = [GunShoot, SniperShoot]
