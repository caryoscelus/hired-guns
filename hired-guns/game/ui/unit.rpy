screen unit_description(unit):
    modal True
    xfill True yfill True
    window:
        xsize 1024 ysize 640
        background "#bbb"
        vbox:
            xfill True
            text "[unit.name]":
                xalign 0.5
            hbox:
                add unit.image or "unknown" zoom 0.5
                text "[unit.description]"
            text "hp: [unit.hp] / [unit.maxhp]"
            text "psy: [unit.psy] / [unit.maxpsy]"
        textbutton "X" xalign 0.0 yalign 0.0 action Hide('unit_description')

label test_unit_description:
    show screen unit_description(game.mercs_named['nya'])
    return
