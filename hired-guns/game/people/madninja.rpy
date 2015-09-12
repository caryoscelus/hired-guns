init python hide:
    madninja = Merc('madninja')
    madninja.name = _('Mad Ninja')
    madninja.set_skill('stealth', 10)
    madninja.set_skill('unarmed_combat', 3)
    madninja.cost = 40
    madninja.maxpsy = 20
    game.add_merc(madninja)
