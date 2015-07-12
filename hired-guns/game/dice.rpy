init python:
    from dracykeiton.common import Dice
    
    def roll_dice(dice):
        action = dice.roll_dice()
        if action:
            action()

screen dice(dice):
    frame:
        has hbox
        text "{}".format(dice.read())
        textbutton "Roll" action Function(roll_dice, dice)
