screen merc_default(merc, action, selected=False):
    button action action:
        has vbox
        text "Merc {}".format(merc.name) bold selected

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
