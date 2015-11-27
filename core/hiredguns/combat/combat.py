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
from dracykeiton.entity import Entity, mod_dep, depends, simplenode
from dracykeiton.common import Name, Wield, Hp, XY
import dracykeiton.random as random
from ..skills import Skills

class Hurt(Entity):
    @unbound
    def _init(self):
        self.dynamic_property('hit_chance', 1.0)
        self.dynamic_property('hit_damage', 0)
        self.dynamic_property('crit_chance', 1.0)

@mod_dep(XY)
class Aim(Entity):
    @unbound
    def _init(self):
        self.dynamic_property('aim_target', None)
        self.dynamic_property('aim_range', None)
    
    @unbound
    def _load(self):
        self.add_get_node('aim_range', self.get_aim_range())
    
    @depends('x', 'y')
    @depends('aim_target')
    @simplenode
    def get_aim_range(value, aim_target, x, y):
        if not aim_target:
            return None
        if None in (x, y, aim_target.x, aim_target.y):
            return None
        return max(abs(x-aim_target.x), abs(y-aim_target.y))
    
    @unbound
    def aim(self, target):
        self.aim_target = target

@mod_dep(Wield, Aim, Hurt)
class AimWeapon(Entity):
    """Adjust hit_damage according to firing distance"""
    @unbound
    def _load(self):
        self.add_get_node('hit_damage', self.get_range_damage())
    
    @depends('aim_range')
    @simplenode
    def get_range_damage(value, aim_range):
        return value

@mod_dep(Wield, Hurt)
class WieldWeapon(Entity):
    """Adjust hit_damage according to wielded weapon"""
    @unbound
    def _load(self):
        self.add_get_node('hit_damage', self.get_base_damage())
    
    @depends('wielded')
    @simplenode
    def get_base_damage(value, wielded):
        if wielded is None:
            return value
        return wielded.base_damage

@mod_dep(Hp)
class HurtBy(Entity):
    @unbound
    def apply_hurt(self, attacker):
        missed = random.random() > attacker.hit_chance
        if missed:
            return
        crit = random.random() > attacker.crit_chance
        damage = attacker.hit_damage * (2**crit)
        self.hurt(damage)


class Accuracy(Entity):
    @unbound
    def _init(self):
        self.dynamic_property('accuracy', 1)

@mod_dep(Skills, Wield, Accuracy)
class WeaponAccuracy(Entity):
    @unbound
    def _load(self):
        self.add_get_node('accuracy', self.get_weapon_accuracy())
    
    @depends('wielded')
    @simplenode
    def get_weapon_accuracy(value, wielded):
        if wielded is None:
            return value
        return value * wielded.base_accuracy

@mod_dep(Accuracy, Hurt)
class AccuracyHitChance(Entity):
    @unbound
    def _load(self):
        self.add_get_node('hit_chance', self.get_accuracy_hit_chance())
    
    @depends('accuracy')
    @simplenode
    def get_accuracy_hit_chance(value, accuracy):
        return value * accuracy

@mod_dep(
    AimWeapon,
    WieldWeapon,
    WeaponAccuracy,
    AccuracyHitChance,
    HurtBy,
)
class Combat(Entity):
    pass


@mod_dep(Name)
class Weapon(Entity):
    @unbound
    def _init(self):
        self.dynamic_property('skill', None)
        self.dynamic_property('level', 0)
        self.dynamic_property('base_accuracy', 1)
        self.dynamic_property('base_damage', 1)
        self.name = 'weapon'
