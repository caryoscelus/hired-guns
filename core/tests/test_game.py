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

""""""

from dracykeiton.compat import *
from dracykeiton.tb.turnman import Turnman
from dracykeiton import pickle
from hiredguns.world import HiredGunsWorld
from hiredguns.merc import Merc
from hiredguns.sandbox import LowMonster
from hiredguns.combat import Gun, SniperRifle, HGBattle, prepare_battle
from hiredguns.utils import new_battle

import pytest

@pytest.fixture
def world():
    pc_name = 'You'
    pc = Merc('pc')
    pc.name = pc_name
    world = HiredGunsWorld(pc)
    return world

def test_battle(world):
    pc = world.pc
    pc.maxap = 5
    pc.put_to_inv(SniperRifle())
    battle = new_battle()
    for i in range(4):
        battle.add_enemy(LowMonster())
    
    manager = prepare_battle(battle)
    
    turnman = manager.turnman
    field = turnman.world
    side = field.sides['pc']
    
    assert pc.x == 0 and pc.y == 0
    
    # select pc and move close to the enemy
    manager.clicked(side, (pc.x, pc.y))
    assert manager.selected is pc
    for i in range(3):
        manager.clicked(side, (pc.x+1, pc.y))
    assert pc.ap == 2
    assert pc.x == 3
    
    manager.hovered(side, (pc.x+1, pc.y))
    manager.clicked_melee()
    assert pc.ap == 0
    
    manager.end_turn()
    assert pc.ap == 5
    
    #world1, manager1, battle = pickle.loads(pickle.dumps([world, manager, battle]))
    #assert world1.pc.xy() == pc.xy()

def test_pickle(world):
    re_world = pickle.loads(pickle.dumps(world))
