screen merc_default(merc, action):
    button action action:
        has vbox
        text "Merc {}".format(merc.name)

init python:
    def dict_toggle(d, key):
        d[key] = not d[key]

screen merc_chooser(mercs):
    default chosen = {merc : False for merc in mercs}
    frame:
        has vbox
        label "Choose mercs.."
        for merc in mercs:
            use merc_default(merc, Function(dict_toggle, chosen, merc))
        textbutton "Ok!" action Return(chosen)
