init python:
    from dracykeiton import random
    from hiredguns.world import HiredGunsWorld
    from hiredguns.mission import Mission
    
    def init_world():
        global world
        world = HiredGunsWorld()
        world.missions.append(Mission('test mission', 'test_mission'))
    
    def random_merc(req_traits=()):
        mercs = [merc for merc in world.active_mission.mercs if merc.has_all_traits(req_traits)]
        if mercs:
            return random.choice(mercs)
        else:
            return None
    
    def selected_merc():
        return world.active_mission.selected
