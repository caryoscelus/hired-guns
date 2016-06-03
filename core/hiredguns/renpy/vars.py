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

from hiredguns.world import HiredGunsWorld
from hiredguns.utils import active_mission

import renpy

def define_var(name, value=None):
    if active_mission():
        active_mission().define_var(name)
    else:
        print('WARNING: no mission; vars defined with define_var will not be cleared')
    setattr(renpy.store, name, value)
    return value
