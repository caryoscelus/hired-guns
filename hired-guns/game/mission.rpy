label mission(mission):
    ">> mission start"
    show screen mission_merc_list(mission)
    if mission.content:
        $ renpy.call(mission.content, mission)
    else:
        "Your mission was a failure"
    hide screen mission_merc_list
    ">> mission end"
    return

label choose_mercs_for_mission(mission):
    call screen merc_chooser(world.mercs)
    $ mission.mercs.update([merc for merc in _return if _return[merc]])
    return

screen mission_merc_list(mission):
    frame:
        xalign 1.0
        has vbox
        if not mission.mercs:
            text "You've got no mercs on mission! You're quite doomed!"
        for merc in mission.mercs:
            use merc_default(merc, mission.select_merc(merc))
