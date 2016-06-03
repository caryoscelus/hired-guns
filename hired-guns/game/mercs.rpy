init python:
    from hiredguns.monster import Monster
    from hiredguns.renpy import mercs
    
    from dracykeiton.util import curry
    def merc_is_selected(merc, mission):
        return merc is mission.selected

screen merc_default(merc, action=None, selected=False, get_selected=None):
    python:
        mission = active_mission()
        if mission:
            if not get_selected:
                get_selected = curry.curry(merc_is_selected)(merc, mission)
            if not action:
                action = Function(mission.select, merc)
    button action action:
        background Solid('#2223')
        has vbox
        if merc.image:
            add merc.image zoom 0.25
        text "hp: {0.hp} / {0.maxhp}".format(merc) style 'ui_small'
        text "psy: {0.psy} / {0.maxpsy}".format(merc) style 'ui_small'
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

screen team_view():
    frame:
        xalign 0.5
        yalign 1.0
        background Solid('#2223')
        has hbox
        $ mission = active_mission()
        for merc in [world.pc]+world.pc.team:
            use merc_default(merc)
