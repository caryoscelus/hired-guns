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

"""Hired-guns specific menu option"""

from .requirements import *
from .abstract_menu import APIAdvancedMenuOption, OutcomeAdvancedMenuOption

class HiredGunsAdvancedMenuOption(APIAdvancedMenuOption, OutcomeAdvancedMenuOption):
    api_classes = list([RequireSkill, RequireTrait, MoneyCost, PsyCost, AffectTrait])
    
    def __init__(self, name):
        super(HiredGunsAdvancedMenuOption, self).__init__()
        self.name = name
        self.roll_n = None
    
    def roll(self, n):
        self.roll_n = n
