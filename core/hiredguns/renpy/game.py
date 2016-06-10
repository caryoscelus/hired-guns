##
##  Copyright (C) 2015-2016 caryoscelus
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

from dracykeiton.compat import *
from dracykeiton.util import globalvars
from collections import OrderedDict

class Game(object):
    def __init__(self):
        self.mercs = OrderedDict()
        self.npcs = OrderedDict()
        self.places = OrderedDict()
        self.default_place = None
    
    def add_merc(self, merc):
        self.mercs[merc.id] = merc
    
    def add_npc(self, npc):
        self.npcs[npc.id] = npc
    
    def add_place(self, place):
        self.places[place.id] = place
    
    def set_default_place(self, place):
        self.default_place = place
    
    def get_place(self, id):
        return self.places[id]

globalvars.set('game', Game())
