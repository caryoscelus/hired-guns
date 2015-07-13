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

"""World for HiredGuns

TODO: split
"""

from dracykeiton.compat import *
from dracykeiton.entity import Entity, mod_dep, simplenode
from dracykeiton.common import RoundingHp

class Name(Entity):
    """Entity with a name"""
    @unbound
    def _init(self, name=''):
        self.dynamic_property('name', name)

class Attitude(Entity):
    """Contains attitude property; default is 0 (neutral)"""
    @unbound
    def _init(self, attitude=0):
        self.dynamic_property('attitude', attitude)

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

NATIONS = ('cosmopolite', 'pleb', 'imp', 'manny')
class Nation(Entity):
    """Reflects owner's nation. Game-specific"""
    @unbound
    def _init(self, nation='cosmopolite'):
        self.dynamic_property('nation', nation)
        self.check_nation()(self, nation)
    
    @unbound
    def _load(self):
        self.add_set_node('nation', self.check_nation())
    
    @simplenode
    def check_nation(value):
        if value in NATIONS:
            return value
        raise ValueError('there is no such nation as {}. try another universe?'.format(value))

TACTICS = ('default', 'cover', 'retreat', 'attack', 'defend')
class Tactics(Entity):
    """Contains basic tactic direction."""
    @unbound
    def _init(self):
        self.dynamic_property('tactic', 'default')
    
    @unbound
    def _load(self):
        self.add_set_node('tactic', self.check_tactic())
    
    @simplenode
    def check_tactic(value):
        if value in TACTICS:
            return value
        raise ValueError('there is no such tactic as {}'.format(value))

class Target(Entity):
    """Target in battle"""
    @unbound
    def _init(self):
        self.dynamic_property('target', None)

@mod_dep(
    # base attributes
    RoundingHp,
    
    # merc stuff
    Name,
    Nation,
    Attitude,
    MercStatus,
    
    # battle
    Tactics,
    Target
)
class Merc(Entity):
    """Main mercenary class"""
    @unbound
    def _init(self, name='merc'):
        self.name = name

class HiredGunsWorld(object):
    def __init__(self):
        self.mercs = list([Merc('nobody')])
        self.missions = list()
