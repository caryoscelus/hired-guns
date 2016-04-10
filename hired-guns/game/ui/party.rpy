# universal party/unit/inventory screen

# states:
# party/unit -> unit/description -> unit/inventory -> inventory/description

init python:
    states = {
        'party' : ('party', 'unit',),
        'unit' : ('unit', 'unit_description',),
        'equip' : ('unit', 'inventory',),
        'inventory' : ('inventory', 'inventory_description'),
    }

screen universal_party(state='party'):
    default left_panel = states[state][0]
    default right_panel = states[state][1]
    drag:
        xalign 0.5 yalign 0.5
        window:
            xsize 1024 ysize 640
            background '#bbb'
            textbutton "X" xalign 0.0 action Hide('universal_party')
            text "[state]" xalign 0.5
            fixed:
                xsize 512 ysize 600
                xoffset 0 yoffset 40
                if left_panel == 'party':
                    use party
                elif left_panel == 'unit':
                    use unit
                elif left_panel == 'unit_description':
                    use unit_description
                elif left_panel == 'inventory':
                    use inventory
                elif left_panel == 'inventory_description':
                    use inventory_description
            fixed:
                xsize 512 ysize 600
                xoffset 512 yoffset 40
                if right_panel == 'party':
                    use party
                elif right_panel == 'unit':
                    use unit
                elif right_panel == 'unit_description':
                    use unit_description
                elif right_panel == 'inventory':
                    use inventory
                elif right_panel == 'inventory_description':
                    use inventory_description

screen party:
    default party = [world.pc] + world.pc.team
    vbox:
        for merc in party:
            use party_member(merc)

screen party_member(merc):
    frame:
        has vbox
        text merc.name

screen unit:
    text "unit"

screen unit_description:
    text "unit_description"

screen inventory:
    text "inventory"

screen inventory_description:
    text "inventory_description"

label test_universal_party:
    show screen universal_party()
    return
