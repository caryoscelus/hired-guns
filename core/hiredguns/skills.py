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

from dracykeiton.compat import *
from dracykeiton.entity import Entity, mod_dep

KNOWN_SKILLS = ('stealth', 'cooking', 'unarmed_combat')

class Skills(Entity):
    @unbound
    def _init(self):
        self.dynamic_property('skills', dict())
    
    @unbound
    def set_skill(self, skill, value):
        if not skill in KNOWN_SKILLS:
            print('WARNING: {} is not known skill!'.format(skill))
        self.skills[skill] = value
    
    @unbound
    def has_skill(self, skill, level=1):
        return self.get_skill(skill) >= level
    
    @unbound
    def get_skill(self, skill):
        return self.skills.get(skill, 0)
