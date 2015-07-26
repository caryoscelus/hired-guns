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
from dracykeiton.entity import Entity
from dracykeiton.tb.controller import UserController, Controller
from dracykeiton.tb.encounter import Encounter
from dracykeiton.tb.turnman import Turnman
from .merc import Merc

class Mission(Entity):
    """Mission
    """
    def _init(self, name, content=None, description='', payment=None):
        self.dynamic_property('name', name)
        self.dynamic_property('content', content)
        self.dynamic_property('description', description)
        self.dynamic_property('payment', payment)
        self.dynamic_property('mercs', set())
        self.dynamic_property('battleman', None)
        self.dynamic_property('selected', None)
        self.dynamic_property('tags', set())
    
    def add_mercs(self, mercs):
        self.mercs.update(mercs)
        for merc in mercs:
            merc.be_born()
    
    def select_merc(self, merc):
        self.selected = merc
    
    def finish(self):
        for merc in self.mercs:
            merc.be_unborn()
        self.mercs = set()
    
    def prepare_battle(self):
        encounter = Encounter(Turnman)
        encounter.add_side('left', UserController, len(self.mercs), predefined=list(self.mercs))
        encounter.add_side('right', Controller, (1, 4), possible=Merc)
