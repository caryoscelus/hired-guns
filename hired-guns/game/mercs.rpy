init python:
    # TODO: move elsewhere?
    from dracykeiton.compat import *
    from dracykeiton.entity import Entity, mod_dep
    from hiredguns.merc import Name, Merc
    
    @mod_dep(Name)
    class MercSpeaker(Entity):
        @unbound
        def _init(self):
            self.dynamic_property('speaker', Character(self.name))
    
    Merc.global_mod(MercSpeaker)

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
