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

"""Mercs attitude system"""

from dracykeiton.compat import *
from dracykeiton.entity import Entity, mod_dep, simplenode

class Attitude(Entity):
    """Contains attitude property; default is 0 (neutral)"""
    @unbound
    def _init(self, attitude=0):
        self.dynamic_property('attitude', attitude)

@mod_dep(Attitude)
class Patriot(Entity):
    @unbound
    def _init(self):
        self.dynamic_property('patriot', 0.0)
    
    @unbound
    def _load(self):
        self.add_set_node('patriot', self.check_patriot())
    
    @simplenode
    def check_patriot(value):
        if -1 <= value <= 1:
            return value
        raise ValueError('one cannot {} his country THAT much (patriot property {} > 1)'.format('hate' if value < -1 else 'love', value))
