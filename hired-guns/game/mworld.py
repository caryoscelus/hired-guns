import renpy
from hiredguns.world import HiredGunsWorld

def define_var(name, value=None):
    HiredGunsWorld.instance().active_mission.define_var(name)
    setattr(renpy.store, name, value)
