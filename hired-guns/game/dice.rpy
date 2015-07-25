init python:
    from dracykeiton.common import Dice
    from dracykeiton import random
    
    def roll_dice(dice):
        action = dice.roll_dice()
        if action:
            action()

screen dice(dice):
    frame:
        has hbox
        text "{}".format(dice.read())
        textbutton "Roll" action Function(roll_dice, dice)

screen roll_dice(result):
    frame:
        text "{}".format(result)

init python:
    def reroll(result):
        for i in range(len(result)):
            result[i] = random.randint(1, 6)
    
    def roll_same(n, result):
        for i in range(len(result)):
            result[i] = n

label roll_dices_action(n, f):
    call screen roll_dices(n)
    $ f(_return)
    return

screen roll_dices(n):
    default result = [random.randint(1, 6) for i in range(n)]
    frame:
        xalign 0.5 yalign 0.5
        has vbox
        hbox:
            for r in result:
                use roll_dice(r)
        hbox:
            textbutton "Re-roll!" action Function(reroll, result)
            textbutton "Roll 1s" action Function(roll_same, 1, result)
            textbutton "Roll 6s" action Function(roll_same, 6, result)
            textbutton "Ok!" action Return(result)
