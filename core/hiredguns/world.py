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
"""

from dracykeiton.compat import *
from .merc import Merc
from .mission import Mission

class HiredGunsWorld(object):
    def __init__(self, pc):
        self.pc = pc
        self.mercs = list()
        self.hired_mercs = list()
        self.missions = dict()
        self.active_mission = None
    
    def add_mission(self, mission):
        self.missions[mission] = 'available'
    
    def start_mission(self, mission):
        mission.add_mercs((self.pc,))
        mission.add_mercs(self.hired_mercs)
        self.hired_mercs = list()
        self.active_mission = mission
        mission.selected = self.pc
        self.missions[mission] = 'active'
    
    def end_mission(self):
        self.active_mission.finish()
        self.missions[self.active_mission] = 'finished'
        self.active_mission = None
