init python:
    from dracykeiton.compat import *
    from hiredguns.world import HiredGunsWorld
    from hiredguns.mission import Mission
    from hiredguns.encounter import Encounter
    from hiredguns.merc import Merc
    from mworld import random_merc, selected_merc, affect_trait, mission_outcome, random_encounter, get_team_skill, spawn_battle, define_var
    
    def init_world():
        #pc_name = renpy.input(_("What is your name?"))
        pc_name = 'pc'
        global world
        world = HiredGunsWorld(Merc(pc_name))
