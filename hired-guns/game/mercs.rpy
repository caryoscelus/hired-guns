init python:
    from hiredguns.monster import Monster
    import mercs

screen merc_default(merc, action, selected=False, get_selected=None):
    button action action style 'filled_frame':
        has vbox
        if merc.image:
            add merc.image zoom 0.25
        text "hp: {0.hp} / {0.maxhp}".format(merc) style 'ui_small'
        text "psy: {0.psy} / {0.maxpsy}".format(merc) style 'ui_small'
        text "attitude: {0.attitude}".format(merc) style 'ui_small'
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
        for merc in [world.pc]+world.pc.team:
            add merc.image zoom PORTRAIT_ZOOM
