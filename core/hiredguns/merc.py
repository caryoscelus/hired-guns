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

"""Merc"""

from dracykeiton.compat import *
from dracykeiton.entity import Entity, mod_dep, simplenode, depends, listener
from .nation import Nation
from .traits import Traits, TraitAttitude, Attitude
from .skills import Skills
from .monster import Monster
from .contacts import Contacts

MERC_STATUSES = ('free', 'busy', 'injured', 'dead')
class MercStatus(Entity):
    """Status of merc for in-between mission display."""
    @unbound
    def _init(self, status='free'):
        self.dynamic_property('merc_status', status)
        self.check_merc_status()(self, status)
    
    @unbound
    def _load(self):
        self.add_set_node('merc_status', self.check_merc_status())
    
    @simplenode
    def check_merc_status(value):
        if value in MERC_STATUSES:
            return value
        raise ValueError('there is no such merc as status as {}.. sorry'.format(value))

@mod_dep(Attitude)
class Hire(Entity):
    @unbound
    def _init(self, cost=0):
        self.dynamic_property('cost', cost)
    
    @unbound
    def hire(self, mission):
        if self.attitude < 0:
            return False
        return True

class Money(Entity):
    @unbound
    def _init(self):
        self.dynamic_property('money', 0)
    
    @unbound
    def pay(self, amount):
        self.money -= amount
    
    @unbound
    def spend_money(self, amount):
        if amount <= self.money:
            self.money -= amount
            return True
        return False

@mod_dep(
    # basic battle stuff
    Monster,
    
    # merc stuff
    Nation,
    MercStatus,
    Traits,
    Skills,
    TraitAttitude,
    Hire,
    Money,
    Contacts,
)
class Merc(Entity):
    """Main mercenary class"""
    @unbound
    def _init(self, name='merc'):
        self.name = name
        self.maxhp = 5
