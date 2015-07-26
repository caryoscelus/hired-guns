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
    
    def roll_skill_hurt(skill, want, atleast, damage):
        renpy.call('roll_skill_hurt', skill, want, atleast, damage)

label roll_skill_hurt(skill, want, atleast, damage):
    $ define_var('remaining_mercs', world.active_mission.mercs.copy())
label roll_skill_hurt_loop:
    if not remaining_mercs:
        jump roll_skill_hurt_end
    $ define_var('merc', remaining_mercs.pop())
    call screen roll_dices(merc.get_skill(skill))
    $ define_var('r', [dice for dice in _return if want[0] <= dice <= want[1]])
    if len(r) < atleast:
        $ merc.hurt(damage)
    jump roll_skill_hurt_loop
label roll_skill_hurt_end:
    return
