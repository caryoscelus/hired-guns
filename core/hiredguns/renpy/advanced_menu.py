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
from dracykeiton.encounter import outcome, advanced_menu

import renpy.exports as renpy
import renpy.store as store

from hiredguns.utils import selected_merc, get_team_skill, affect_trait
from hiredguns.encounter.advanced_menu import HiredGunsOption

class RenpyLabelOutcome(outcome.LabelOutcome):
    def launch(self):
        renpy.call(self.label)

class AdvancedMenuOption(HiredGunsOption):
    outcome_class = RenpyLabelOutcome
    def call_roll(self, n):
        renpy.call('roll_dices_action', self.roll_n, self.after_roll)

class AdvancedMenu(advanced_menu.AdvancedMenu):
    option_class = AdvancedMenuOption

store.am = AdvancedMenu()
