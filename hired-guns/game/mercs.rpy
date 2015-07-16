init python:
    # TODO: move elsewhere?
    from dracykeiton.compat import *
    from dracykeiton.entity import Entity, mod_dep, listener
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

screen merc_default(merc, action, selected=False, get_selected=None):
    button action action:
        has vbox
        text "Merc {}".format(merc.name) bold (get_selected() if get_selected else selected)

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
