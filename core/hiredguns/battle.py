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

"""Battle state & other related stuff"""

from dracykeiton.compat import *
from dracykeiton.entity import Entity, listener, mod_dep
from dracykeiton.common import SimpleField
from dracykeiton.tb.controller import UserController, Controller
from dracykeiton.tb.battlegen import BattleGen
from dracykeiton.ui.battleuimanager import BattleUIManager
from .tactics import BattleTactic

class HGBattleAIController(Controller):
    pass

class HGBattle(object):
    def __init__(self, turnman_c, world):
        self.gen = BattleGen(turnman_c)
        self.world = world
        self.enemies = list()
    
    def add_enemy(self, enemy):
        self.enemies.append(enemy)
    
    def generate(self):
        mercs = self.world.active_mission.mercs
        self.gen.add_side('pc', UserController, len(mercs), predefined=mercs)
        self.gen.add_side('enemy', HGBattleAIController, len(self.enemies), predefined=self.enemies)
        return self.gen.generate()

class HGBattleUIManager(BattleUIManager):
    def get_tactics(self, entity):
        return [BattleTactic('defend'), BattleTactic('attack')]
    
    def set_tactic(self, side, entity, tactic):
        if self.active_controller().entity == side:
            def f():
                entity.tactic = tactic
            return f
        else:
            return None
