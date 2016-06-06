label mission(mission):
    $ world.start_mission(mission)
    hide screen main_view
    show screen team_npc_view()
    if mission.content:
        $ renpy.call(mission.content, mission)
    else:
        "Your mission was a failure"
    hide screen team_npc_view
    $ mission.destroy_vars()
    $ world.end_mission()
    return

label choose_mercs_for_mission(mission):
    $ available_mercs = set(world.mercs)-mission.mercs
    call screen hire_mercs(mission, available_mercs)
    $ mission.add_mercs([merc for merc in _return if _return[merc]])
    return
