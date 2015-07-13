screen expandable(text):
    default expanded = False
    frame:
        has vbox
        textbutton text action ToggleScreenVariable('expanded')
        if expanded:
            transclude

screen debug_all(world):
    #use expandable("Debug.."):
    default expanded = False
    default dice = Dice(6)
    frame:
        has vbox
        textbutton "Debug.." action ToggleScreenVariable('expanded')
        if expanded:
            use debug_mercs(world.mercs)
            use debug_missions(world.missions)
            use dice(dice)

screen debug_missions(missions):
    label "Mission list:"
    if not missions:
        label "There are none.. Good job!"
    for mission in missions:
        use debug_mission(mission)

screen debug_mission(mission):
    frame:
        has vbox
        label "Mission"
        #use debug_entity(mission)
        textbutton 'Start mission' action Function(renpy.call, 'mission', mission)

screen debug_mercs(mercs):
    #use expandable("Merc list"):
    label "Merc list:"
    if not mercs:
        label "There are none.. O_o"
    for merc in mercs:
        use debug_merc(merc)

screen debug_merc(merc):
    frame:
        has vbox
        label "Merc"
        use debug_entity(merc)

screen debug_entity(entity):
    frame:
        has vbox
        label "All properties"
        for prop in entity._props:
            label '{} : {}'.format(prop, getattr(entity, prop))
