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
            use dice(dice)

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
        frame:
            has vbox
            label "All properties"
            for prop in merc._props:
                label '{} : {}'.format(prop, getattr(merc, prop))
