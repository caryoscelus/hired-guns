label mission(mission):
    $ world.start_mission(mission)
    show screen mission_merc_list(mission)
    if mission.content:
        $ renpy.call(mission.content, mission)
    else:
        "Your mission was a failure"
    hide screen mission_merc_list
    $ world.end_mission()
    return

label choose_mercs_for_mission(mission):
    $ available_mercs = set(world.mercs)-mission.mercs
    call screen hire_mercs(mission, available_mercs)
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
