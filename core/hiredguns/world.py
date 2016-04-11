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
from .time import Time, DAY

class AlmostSingleton(object):
    _instance = None
    def __new__(cl, *args, **kwargs):
        self = super(AlmostSingleton, cl).__new__(cl, *args, **kwargs)
        if not cl._instance:
            cl._instance = self
        return self
    
    @classmethod
    def instance(cl):
        return cl._instance

class HiredGunsWorld(AlmostSingleton):
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
        self.now_place = None
        self.default_place = None
    
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
    
    def goto(self, place):
        self.now_place = place
    
    def get_mission_by_label(self, label):
        try:
            return [m for m in self.mission_pool.keys()+self.missions if m.content == label][0]
        except IndexError:
            raise ValueError('mission with label "{}" not found'.format(label))
    
    def start_mission(self, mission):
        mission.add_mercs((self.pc,))
        for merc in self.hired_mercs:
            self.pc.pay(merc.cost)
            mission.add_mercs((merc,))
        self.hired_mercs = list()
        self.active_mission = mission
        mission.selected = self.pc
    
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
        ## TODO
        self.pc.cleanup_tickets(self.time)
    
    def pass_time_until(self, time):
        while time.t > self.time.t:
            self.pass_day()
