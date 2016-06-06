init python:
    def merc_is_selected(merc, mission):
        return merc is mission.selected

screen character_default(char, action=None, selected=False, get_selected=None):
    python:
        mission = active_mission()
        if mission:
            if not get_selected:
                get_selected = curry.curry(char_is_selected)(char, mission)
            if not action:
                action = Function(mission.select, char)
    button action action:
        background Solid('#eee3')
        xsize 128 ysize 160
        xpadding 0 ypadding 0
        vbox:
            xalign 1.0
            if char.has_mod(Merc):
                text "hp {0.hp} / {0.maxhp}".format(char) style 'ui_small'
                text "psy {0.psy} / {0.maxpsy}".format(char) style 'ui_small'
        text char.name:
            bold (get_selected() if get_selected else selected)
            yalign 0.0
        if char.image:
            add char.image zoom 0.25 yalign 1.0

screen merc_chooser(mercs):
    default chosen = {merc : False for merc in mercs}
    frame:
        xalign 0.5
        yalign 0.5
        has vbox
        label "Choose mercs.."
        for merc in mercs:
            use character_default(merc, ToggleDict(chosen, merc), chosen[merc])
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

screen characters_view(characters):
    frame:
        xalign 0.5
        yalign 1.0
        background Solid('#2226')
        has hbox
        spacing 4
        for char in characters:
            use character_default(char)

screen team_view():
    use characters_view([world.pc]+world.pc.team)

screen npc_view():
    use characters_view(current_scene().npcs)

screen team_npc_view():
    hbox:
        xalign 0.5 yalign 1.0
        spacing 10
        use team_view()
        use npc_view()
