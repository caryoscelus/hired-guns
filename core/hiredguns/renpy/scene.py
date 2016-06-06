##
##  Copyright (C) 2016 caryoscelus
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

class Scene(object):
    def __init__(self):
        self.npcs = list()
    
    def add_npc(self, npc):
        self.npcs.append(npc)
    
    def remove_npc(self, npc):
        self.npcs.remove(npc)
    
    def clear_npcs(self):
        self.npcs = list()

def current_scene():
    return globalvars.get('_current_scene')

def clear_scene():
    current_scene().clear_npcs()

globalvars.set('_current_scene', Scene())
