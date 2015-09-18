init python hide:
    madninja = Merc('madninja')
    madninja.name = _('Mad Ninja')
    madninja.set_skill('stealth', 10)
    madninja.set_skill('unarmed_combat', 3)
    madninja.cost = 40
    madninja.maxpsy = 20
    madninja.description = _("""A mad ninja. Or maybe not ninja at all, but still pretty mad.""")
    madninja.add_preference('weaponshop', 10)
    madninja.add_preference('restaurant', -5)
    game.add_merc(madninja)
