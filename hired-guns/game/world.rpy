init python:
    from dracykeiton.compat import *
    from hiredguns.world import HiredGunsWorld
    from hiredguns.mission import Mission
    from hiredguns.merc import Merc
    from mworld import random_merc, selected_merc, affect_trait
    
    def init_world():
        #pc_name = renpy.input(_("What is your name?"))
        pc_name = 'pc'
        global world
        world = HiredGunsWorld(Merc(pc_name))
