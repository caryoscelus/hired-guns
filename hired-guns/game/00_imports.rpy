init -5 python:
    from dracykeiton.compat import *
    
    from dracykeiton.util import curry
    
    from dracykeiton.common.dice import get_dice
    
    import hiredguns.renpy.mercs
    
    from hiredguns.monsters import *
    
    from hiredguns.world import HiredGunsWorld
    from hiredguns.mission import Mission
    from hiredguns.encounter.encounter import Encounter
    from hiredguns.merc import Merc
    from hiredguns.contacts import Contact
    from hiredguns.places import Place
    
    from hiredguns.combat import prepare_battle
    
    from hiredguns.renpy.style import apply_margins, VNMode, init_vn_modes, vn_mode, push_mode, set_window_margins, set_window_position, set_text_color, pop_mode, CombinedCharacter
    
    from hiredguns.utils import random_merc, selected_merc, affect_trait, mission_outcome, random_encounter, get_team_skill, new_battle, active_mission
    from hiredguns.renpy.vars import define_var
