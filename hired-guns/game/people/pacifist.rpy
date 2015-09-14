init python hide:
    pacifist = Merc('pacifist')
    pacifist.name = _("Pacifist")
    pacifist.set_skill('stealth', 4)
    pacifist.add_trait('pacifist')
    pacifist.maxpsy = 15
    pacifist.cost = 20
    game.add_merc(pacifist)
