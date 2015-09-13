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
from dracykeiton import random
from .merc import Merc
from .mission import Mission

DAY = 24*60*60
MONTH = 30
YEAR = 12

class Time(object):
    def __init__(self, time=0):
        self.t = time
    
    def __lt__(self, other):
        return self.t < other.t
    
    def __gt__(self, other):
        return self.t > other.t
    
    def __eq__(self, other):
        return self.t == other.t
    
    def __ne__(self, other):
        return self.t != other.t
    
    def __str__(self):
        return '{:04}-{:02}-{:02}'.format(self.year(), self.month()+1, self.day()+1)
    
    def year(self):
        return self.t // (DAY*MONTH*YEAR)
    
    def month(self):
        return self.t // (DAY*MONTH) % YEAR
    
    def day(self):
        return self.t // DAY % MONTH
    
    def pass_time(self, amount):
        self.t += amount

class HiredGunsWorld(object):
    def __init__(self, pc):
        self.pc = pc
        self.mercs = list()
        self.hired_mercs = list()
        self.mission_pool = dict()
        self.missions = list()
        self.places = list()
        self.old_missions = dict()
        self.active_mission = None
        self.encounter_pool = set()
        self.time = Time()
    
    def add_mission(self, mission):
        self.mission_pool[mission] = 'available'
    
    def update_missions(self):
        for mission in self.missions:
            if mission.timeout is None or mission.timeout < self.time:
                self.finish_mission(mission, 'timeout')
        while len(self.missions) < 4 and self.mission_pool:
            mission = random.choice(self.mission_pool.keys())
            del self.mission_pool[mission]
            self.missions.append(mission)
    
    def start_mission(self, mission):
        mission.add_mercs((self.pc,))
        for merc in self.hired_mercs:
            self.pc.pay(merc.cost)
            mission.add_mercs((merc,))
        self.hired_mercs = list()
        self.active_mission = mission
        mission.selected = self.pc
        self.missions[mission] = 'active'
    
    def finish_mission(self, mission, reason):
        self.missions.remove(mission)
        self.old_missions[mission] = reason
    
    def end_mission(self):
        self.active_mission.finish()
        self.finish_mission(self.active_mission, 'finished')
        self.active_mission = None
    
    def get_money_prediction(self):
        return self.pc.money - sum([merc.cost for merc in self.hired_mercs])
    
    def pass_day(self):
        self.time.pass_time(DAY)
        self.update_missions()
