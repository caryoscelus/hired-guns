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
from dracykeiton.tb.controller import UserController, Controller
from dracykeiton.tb.battlegen import BattleGen
from dracykeiton.ui.battleuimanager import BattleUIManager
from dracykeiton.common.battlefield import GridField
from .tactics import BattleTactic
from .combat import Weapon

class HGBattleAIController(Controller):
    pass

@mod_dep(GridField)
class HGField(Entity):
    @unbound
    def _init(self, w=1, h=1):
        self.init_grid(w, h)
    
    @unbound
    def perform_action(self, actor, target, tool):
        if tool.has_mod(Weapon):
            target.get().hurt(tool.power)

class HGBattle(object):
    def __init__(self, turnman_c, world):
        self.gen = BattleGen(turnman_c, HGField, w=5, h=4)
        self.world = world
        self.enemies = list()
    
    def add_enemy(self, enemy):
        self.enemies.append(enemy)
    
    def generate(self):
        mercs = [self.world.pc]+self.world.pc.team
        self.gen.add_side('pc', UserController, len(mercs), predefined=mercs)
        self.gen.add_side('enemy', HGBattleAIController, len(self.enemies), predefined=self.enemies)
        return self.gen.generate()

class HGBattleUIManager(BattleUIManager):
    def start(self):
        self.spawn_side('pc', 'left')
        self.spawn_side('enemy', 'right')
        super(HGBattleUIManager, self).start()
    
    def spawn_side(self, who, where):
        field = self.turnman.world
        w, h = field.size
        where_d = {
            'left' : (0, 1),
            'right' : (w*h-1, -1),
        }
        i, k = where_d[where]
        for merc in field.sides[who].members:
            x, y = i / h, i % h
            field.put_on(x, y, merc)
            i += k
    
    def clicked(self, side, xy):
        """Process simple click on battle cell.
        
        Right now, it can do following:
            * select/deselect player entity
            * move player entity to free cell
        """
        field = self.turnman.world
        x, y = xy
        cell = field.grid[y][x]
        merc = cell.get()
        if self.selected:
            if self.selected is merc:
                self.deselect()
            elif merc is None:
                self.do_action(self.selected.move(x, y))
        else:
            if side is self.active_controller().entity:
                self.selected = merc
    
    def hovered(self, side, xy):
        """Process hover on battle cell.
        """
        if self.selected:
            x, y = xy
            cell = self.turnman.world.grid[y][x]
            self.selected.aim(cell)
    
    def clicked_inventory(self, merc, item):
        """Process clicking on inventory item"""
        merc.wield(item)
    
    def get_combat_actions(self):
        if self.selected:
            return self.selected.known_actions
        return ()
    
    def hovered_action(self, action):
        self.selected.plan_action(action)
    
    def unhovered_action(self, action):
        if action is self.selected.action_mod:
            self.selected.plan_action(None)
    
    def clicked_action(self, action):
        self.hovered_action(action)
        self.do_action(self.selected.combat_action())
