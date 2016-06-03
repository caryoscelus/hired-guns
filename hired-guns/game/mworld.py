import renpy
from hiredguns.world import HiredGunsWorld
from hiredguns.utils import active_mission

def define_var(name, value=None):
    if active_mission():
        active_mission().define_var(name)
    else:
        print('WARNING: no mission; vars defined with define_var will not be cleared')
    setattr(renpy.store, name, value)
    return value
