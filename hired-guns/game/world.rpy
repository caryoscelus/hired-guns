# import our modules
init python:
    from hiredguns.world import HiredGunsWorld
    from hiredguns.mission import Mission

label init_world:
    $ world = HiredGunsWorld()
    $ world.missions.append(Mission('test mission', 'test_mission'))
