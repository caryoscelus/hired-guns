init python:
    # TODO: move elsewhere?
    from dracykeiton.compat import *
    from dracykeiton.entity import Entity, mod_dep, listener, depends, simplenode
    from dracykeiton import random
    from dracykeiton.common import Name
    from hiredguns.merc import Merc
    from hiredguns.monster import Monster
    from hiredguns.traits import Attitude
    
    @mod_dep(Name)
    class MercSpeaker(Entity):
        @unbound
        def _init(self):
            self.dynamic_property('speaker', CombinedCharacter(self.name))
    
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
            self.image = 'merc{:02}'.format(random.randint(0, 18))
        
        @depends('visual_state')
        @simplenode
        def get_image(value, visual_state):
            if not value:
                return 'merc'
            return value
    
    Monster.global_mod(VisualEntity)

screen merc_default(merc, action, selected=False, get_selected=None):
    button action action style 'filled_frame':
        has vbox
        if merc.image:
            add merc.image zoom 0.333
        text "hp: {0.hp} / {0.maxhp}".format(merc)
        text "psy: {0.psy} / {0.maxpsy}".format(merc)
        text "attitude: {0.attitude}".format(merc)
        text merc.name bold (get_selected() if get_selected else selected)

screen merc_chooser(mercs):
    default chosen = {merc : False for merc in mercs}
    frame:
        xalign 0.5
        yalign 0.5
        has vbox
        label "Choose mercs.."
        for merc in mercs:
            use merc_default(merc, ToggleDict(chosen, merc), chosen[merc])
        textbutton "Ok!" action Return(chosen)

init python:
    def hire_merc(merc, mission, result):
        hired = merc.hire(mission)
        result[merc] = hired

screen hire_merc(merc, mission, result):
    button action Function(hire_merc, merc, mission, result) style 'filled_frame':
        has vbox
        text "Hire [merc.name]" bold result[merc]
        if merc.image:
            add merc.image zoom 0.333

screen hire_mercs(mission, mercs):
    default chosen = {merc : False for merc in mercs}
    frame:
        xalign 0.5
        yalign 0.5
        has vbox
        text "Hire mercs!"
        hbox:
            for merc in mercs:
                use hire_merc(merc, mission, chosen)
        textbutton "Ok!" action Return(chosen)
