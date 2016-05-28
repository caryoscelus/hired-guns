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

"""Battle state & other related stuff"""

from dracykeiton.compat import *
from dracykeiton.entity import Entity, listener, mod_dep, properties
from dracykeiton.tb.controller import UserController, Controller
from dracykeiton.tb.battlegen import BattleGen
from dracykeiton.common import GridField, FieldRange
from dracykeiton.util import curry
from .combat import Weapon
from .manager import HGBattleUIManager

class HGBattleAIController(Controller):
    def act(self):
        for entity in self.entity.members:
            if entity.intellect == 0:
                to_do = entity.act()
                if to_do:
                    return to_do
            else:
                raise NotImplementedError('smart AI is not implemented')
        return None

@properties(joined_cells=set)
@mod_dep(GridField)
class HGField(Entity):
    @unbound
    def _init(self, size=None):
        if size:
            self.set_size(*size)
    
    @unbound
    def get_range(self, axy, bxy):
        if (axy, bxy) in self.joined_cells:
            return 0
        else:
            return abs(axy[0]-bxy[0])+abs(axy[1]-bxy[1])
    
    @unbound
    def join_cells(self, axy, bxy):
        """Join two cells so that distance between them is zero
        
        `axy` and `bxy` should be coordinate tuples (x, y)
        """
        self.joined_cells.add((axy, bxy))
    
    @unbound
    def unjoin_cells(self, axy, bxy):
        self.joined_cells.remove((axy, bxy))

class HGBattle(object):
    def __init__(self, turnman_c, world):
        self.gen = BattleGen(turnman_c, HGField, size=(5, 4))
        self.world = world
        self.enemies = list()
    
    def add_enemy(self, enemy):
        self.enemies.append(enemy)
    
    def generate(self):
        mercs = [self.world.pc]+self.world.pc.team
        self.gen.add_side('pc', UserController, len(mercs), predefined=mercs)
        self.gen.add_side('enemy', HGBattleAIController, len(self.enemies), predefined=self.enemies)
        return self.gen.generate()

def prepare_battle(battle):
    turnman = battle.generate()
    turnman.world.add_lose_condition('pc', curry.curry(check_if_empty)())
    turnman.world.add_lose_condition('enemy', curry.curry(check_if_empty)())
    manager = HGBattleUIManager(turnman)
    manager.start()
    return manager

def check_if_dead(e, side):
    return e.living == 'dead'

def check_if_empty(side):
    return side.empty_side()
