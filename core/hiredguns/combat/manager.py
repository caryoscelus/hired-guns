##
##  Copyright (C) 2016 caryoscelus
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
from dracykeiton.ui.battleuimanager import BattleUIManager
from .melee import MeleeGrab, MeleeFlee

class KeyManager(object):
    """Handles keyboard shortcuts"""
    def __init__(self, manager):
        super(KeyManager, self).__init__()
        self.manager = manager
    
    def offset_merc(self, n):
        mercs = self.manager.turnman.world.sides['pc'].members
        try:
            index = mercs.index(self.manager.selected)
            index = (index+n)%len(mercs)
        except ValueError:
            index = 0
        self.manager.select_merc(mercs[index])
    
    def next_merc(self):
        self.offset_merc(+1)
    
    def prev_merc(self):
        self.offset_merc(-1)
    
    def active_offset(self, dx, dy):
        if not self.manager.active_cell:
            r = (0, 0)
        else:
            x, y = self.manager.active_cell
            w, h = self.manager.turnman.world.size
            r = ((x+dx)%w, (y+dy)%h)
        self.manager.hovered(None, r)
    
    def active_up(self):
        self.active_offset(0, -1)
    
    def active_down(self):
        self.active_offset(0, 1)
    
    def active_left(self):
        self.active_offset(-1, 0)
    
    def active_right(self):
        self.active_offset(1, 0)
    
    def offset_weapon(self, n):
        if not self.manager.selected:
            return
        inv = self.manager.inventory(self.manager.selected)
        try:
            index = inv.index(self.manager.selected.wielded)
            index = (index+n)%len(inv)
        except ValueError:
            index = 0
        self.manager.clicked_inventory(self.manager.selected, inv[index])
    
    def prev_weapon(self):
        """Selected: wield previous weapon"""
        self.offset_weapon(-1)
    
    def next_weapon(self):
        """Selected: wield next weapon"""
        self.offset_weapon(+1)

class HGBattleUIManager(BattleUIManager):
    def __init__(self, *args, **kwargs):
        super(HGBattleUIManager, self).__init__(*args, **kwargs)
        self.active_cell = None
        self.keys = KeyManager(self)
    
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
            x, y = i // h, i % h
            field.put_on(x, y, merc)
            i += k
    
    def select_merc(self, merc):
        self.selected = merc
    
    def clicked(self, side, xy):
        """Process simple click on battle cell.
        
        Right now, it can do following:
            * select/deselect player entity
            * move player entity to free cell
        """
        field = self.turnman.world
        x, y = xy
        cell = field.grid[(x, y)]
        merc = cell.get()
        if self.selected:
            if self.selected is merc:
                self.deselect()
            elif merc is None:
                self.do_action(self.selected.move(x, y))
        else:
            if side is self.active_controller().entity:
                self.select_merc(merc)
    
    def hovered(self, side, xy):
        """Process hover on battle cell.
        """
        self.active_cell = xy
        if self.selected:
            x, y = xy
            cell = self.turnman.world.grid[(x, y)]
            self.selected.aim(cell)
    
    def inventory(self, merc):
        return [None]+merc.inv
    
    def clicked_inventory(self, merc, item):
        """Process clicking on inventory item"""
        merc.wield(item)
    
    def get_combat_actions(self):
        if self.selected:
            return self.selected.known_actions
        return ()
    
    def hovered_action(self, action):
        self.selected.plan_action_mod(action)
    
    def unhovered_action(self, action):
        if action is self.selected.action_mod:
            self.selected.plan_action_mod(None)
    
    def clicked_action(self, action):
        self.hovered_action(action)
        self.do_action(self.selected.combat_action())
        self.unhovered_action(action)
    
    def hovered_melee(self):
        self.selected.plan_action_mod(self.change_melee_action())
    
    def unhovered_melee(self):
        if self.selected.action_mod in [MeleeGrab, MeleeFlee]:
            self.selected.plan_action_mod(None)
    
    def clicked_melee(self):
        self.hovered_melee()
        self.do_action(self.selected.melee_action())
        self.unhovered_melee()
    
    def change_melee_action(self):
        if self.selected:
            # TODO: refactor; this conditions are already in MeleeGrab/Flee
            if self.selected.aim_range == 0 and self.selected.xy() != self.selected.aim_target.xy():
                return MeleeFlee
            elif self.selected.aim_range == 1:
                return MeleeGrab
        return False
