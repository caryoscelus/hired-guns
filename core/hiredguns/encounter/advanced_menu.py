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

from dracykeiton.encounter import option, outcome

from .requirements import *

class HiredGunsOption(option.APIOption, option.RollOutcomeOption):
    api_classes = list([RequireSkill, RequireTrait, MoneyCost, PsyCost, AffectTrait])
    outcome_class = outcome.LabelOutcome
    
    def __init__(self, name):
        super(HiredGunsOption, self).__init__()
        self.name = name
