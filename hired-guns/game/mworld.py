import renpy
from hiredguns.world import HiredGunsWorld

def define_var(name, value=None):
    if HiredGunsWorld.instance().active_mission:
        HiredGunsWorld.instance().active_mission.define_var(name)
    else:
        print('WARNING: no mission; vars defined with define_var will not be cleared')
    setattr(renpy.store, name, value)
    return value
