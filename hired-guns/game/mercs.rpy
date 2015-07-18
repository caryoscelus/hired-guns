init python:
    # TODO: move elsewhere?
    from dracykeiton.compat import *
    from dracykeiton.entity import Entity, mod_dep, listener, depends, simplenode
    from dracykeiton import random
    from hiredguns.merc import Name, Merc
    from hiredguns.traits import Attitude
    
    @mod_dep(Name)
    class MercSpeaker(Entity):
        @unbound
        def _init(self):
            self.dynamic_property('speaker', Character(self.name))
    
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
                self.speaker(_("I am angry at you! I won't work with such a bastard anymore!"))
    
    Merc.global_mod(AttitudeChange)
    
    class VisualEntity(Entity):
        @unbound
        def _init(self):
            self.dynamic_property('image')
            self.dynamic_property('visual_state', 'default')
            self.add_get_node('image', self.get_image())
            self.image = 'merc0{}'.format(random.randint(0, 3))
        
        @depends('visual_state')
        @simplenode
        def get_image(value, visual_state):
            if not value:
                return 'merc'
            return value
    
    Merc.global_mod(VisualEntity)

screen merc_default(merc, action, selected=False, get_selected=None):
    button action action style 'filled_frame':
        has vbox
        if merc.image:
            add merc.image zoom 0.66
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
            add merc.image zoom 0.66

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
