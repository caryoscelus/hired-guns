# TODO: move elsewhere?
from dracykeiton.compat import *
from dracykeiton.entity import Entity, mod_dep, listener, depends, simplenode
from dracykeiton import random
from dracykeiton.common import Name
from hiredguns.merc import Merc
from hiredguns.monster import Monster
from hiredguns.traits import Attitude

import renpy
from style import CombinedCharacter

@mod_dep(Name)
class MercSpeaker(Entity):
    @unbound
    def _init(self):
        self.dynamic_property('speaker', CombinedCharacter(self.name))
        self.add_listener_node('name', self.name_changed())
    
    @listener
    def name_changed(self, target, value):
        self.speaker = CombinedCharacter(self.name)

Merc.global_mod(MercSpeaker)

@mod_dep(Attitude, MercSpeaker)
class AttitudeChange(Entity):
    """Show message when attitude has changed"""
    @unbound
    def _load(self):
        self.add_listener_node('attitude', self.attitude_changed())
    
    @listener
    def attitude_changed(self, target, value):
        if value < 0:
            renpy.notify(_("{} is angry at you and won't work with such a bastard anymore!".format(self.name)))
            
            ## NOTE: this is preferred, but may cause "Cannot start an interaction in the middle of an interaction" error
            #self.speaker(_("I am angry at you! I won't work with such a bastard anymore!"))

Merc.global_mod(AttitudeChange)

class VisualEntity(Entity):
    @unbound
    def _init(self):
        self.dynamic_property('image')
        self.dynamic_property('visual_state', 'default')
        self.add_get_node('image', self.get_image())
    
    @depends('visual_state')
    @depends('id')
    @simplenode
    def get_image(value, visual_state, id):
        if not value:
            return id
        return value

Monster.global_mod(VisualEntity)
