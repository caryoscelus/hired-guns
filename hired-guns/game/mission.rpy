label mission(mission):
    ">> mission start"
    $ world.start_mission(mission)
    show screen mission_merc_list(mission)
    if mission.content:
        $ renpy.call(mission.content, mission)
    else:
        "Your mission was a failure"
    hide screen mission_merc_list
    $ world.end_mission()
    ">> mission end"
    return

label choose_mercs_for_mission(mission):
    call screen merc_chooser(set(world.mercs)-mission.mercs)
    $ mission.add_mercs([merc for merc in _return if _return[merc]])
    return

init python:
    from dracykeiton.util import curry
    def merc_is_selected(merc, mission):
        return merc is mission.selected

screen mission_merc_list(mission):
    frame:
        xalign 1.0
        has vbox
        if not mission.mercs:
            text "You've got no mercs on mission! You're quite doomed!"
        for merc in mission.mercs:
            use merc_default(merc, Function(mission.select_merc, merc), get_selected=curry.curry(merc_is_selected)(merc, mission))
