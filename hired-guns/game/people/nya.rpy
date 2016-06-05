init python hide:
    self = Merc('nya')
    self.name = _("Nya")
    self.description = """A cybercat you know for a very long time
    """
    self.set_skills(
        resilience  = 20,
        dexterity   = 30,
        strength    = 18,
        mind        = 24,
        speed       = 30,
        
        telepathy   = 4,
        hacking     = 7,
        unarmed     = 3,
    )
    self.maxap = 5
    self.cost = 0
    game.add_merc(self)
