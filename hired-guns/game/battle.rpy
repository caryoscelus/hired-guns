screen battle(manager):
    if manager:
        $ turnman = manager.turnman
        frame:
            has vbox
            text "It's {}'s turn".format(turnman.next_side().ally_group)
            grid 2 1:
                xfill True
                frame:
                    xalign 0.0
                    has vbox
                    label "left"
                    use battle_side(manager, turnman.world.sides['left'])
                frame:
                    xalign 1.0
                    has vbox
                    label "right"
                    use battle_side(manager, turnman.world.sides['right'])
            button:
                text "Roll!"
    textbutton "Force quit" yalign 1.0 action Return()

screen battle_side(manager, side):
    text "battle side"
