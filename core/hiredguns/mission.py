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

"""Mission"""

from dracykeiton.compat import *
from dracykeiton.entity import Entity, mod_dep, properties
from dracykeiton.tb.controller import UserController, Controller
from dracykeiton.tb.battlegen import BattleGen
from dracykeiton.tb.turnman import Turnman
from dracykeiton.common import Name, Description, Tags, LocalVariables, Select, Payment
from .merc import Merc

@properties(mercs=set)
class MercContainer(Entity):
    def add_mercs(self, mercs):
        self.mercs.update(mercs)
        for merc in mercs:
            merc.be_born()
    
    def finish(self):
        for merc in self.mercs:
            merc.be_unborn()
        self.mercs = set()

@mod_dep(
    Name,
    Description,
    Tags,
    LocalVariables,
    MercContainer,
    Select,
    Payment,
)
class Mission(Entity):
    """Mission
    
    TODO: Duh, cleanup this mess
    """
    def _init(self, name, content=None, description='', payment=0, timeout=None):
        self.name = name
        self.payment = payment
        self.dynamic_property('content', content)
        self.dynamic_property('timeout', timeout)
        self.dynamic_property('place', None)
