init python:
    from dracykeiton import random
    from hiredguns.world import HiredGunsWorld
    from hiredguns.mission import Mission
    from hiredguns.merc import Merc
    
    def init_world():
        pc_name = renpy.input(_("What is your name?"))
        global world
        world = HiredGunsWorld(Merc(pc_name))
    
    def random_merc(req_traits=()):
        mercs = [merc for merc in world.active_mission.mercs if merc.has_all_traits(req_traits)]
        if mercs:
            return random.choice(mercs)
        else:
            return None
    
    def selected_merc():
        return world.active_mission.selected
