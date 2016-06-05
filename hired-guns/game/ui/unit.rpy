screen unit_description(unit, mode='invisible'):
    drag:
        xalign 0.5 yalign 0.5
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
                
                hbox:
                    frame:
                        xsize 300
                        if mode != 'invisible':
                            use unit_inventory(unit, edit=(mode == 'self'))
                    frame:
                        xsize 300
                        if mode != 'invisible':
                            use unit_skills(unit, edit=(mode =='self'))
            
            textbutton "X" xalign 0.0 yalign 0.0 action Hide('unit_description')

screen unit_inventory(unit, edit=False):
    vbox:
        text "Inventory"
        for item in unit.inv:
            textbutton "[item.name]":
                background "#333"
                action None

screen unit_skills(unit, edit=False):
    vbox:
        text "Skills"
        for skill in unit.skills:
            $ value = unit.get_skill(skill)
            hbox:
                textbutton "[skill]":
                    background "#333"
                    action None
                text "[value]"

label test_unit_description:
    show screen unit_description(game.mercs_named['nya'])
    return
