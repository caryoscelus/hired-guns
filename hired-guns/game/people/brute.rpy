init python hide:
    brute = Merc('brute')
    brute.name = _("Brute")
    brute.set_skill('unarmed', 12)
    brute.maxpsy = 5
    brute.cost = 30
    brute.add_preference('weaponshop', 8)
    game.add_merc(brute)
