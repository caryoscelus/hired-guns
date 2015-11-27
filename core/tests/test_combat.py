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

"""Test combat stuff"""

from dracykeiton.compat import *
from dracykeiton.entity import Entity, mod_dep
from hiredguns.combat import Combat, Gun

@mod_dep(Combat)
class Monster(Entity):
    pass

def test_values():
    aggressor = Monster()
    aggressor.x = 0
    aggressor.y = 0
    victim = Monster()
    weapon = Gun()
    aggressor.wield(weapon)
    
    weapon.base_damage = 10
    weapon.base_accuracy = 0.5
    
    victim.x = 1
    victim.y = 0
    aggressor.aim(victim)
    assert aggressor.hit_chance == 0.5
    assert aggressor.hit_damage == 10
    
    weapon.base_accuracy = 0.8
    assert aggressor.hit_chance == 0.8

def test_hurt():
    aggressor = Monster()
    victim = Monster()
    victim.be_born()
    weapon = Gun()
    aggressor.wield(weapon)
    weapon.base_damage = 1
    weapon.base_accuracy = 1.0
    aggressor.aim(victim)
    assert victim.hp == victim.maxhp
    victim.hurt_by(aggressor)
    assert victim.hp < victim.maxhp
