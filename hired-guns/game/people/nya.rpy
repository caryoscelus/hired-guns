init python hide:
    self = Merc('nya')
    self.name = _("Nya")
    self.description = """A cybercat you know for a very long time
    """
    self.set_skill('unarmed_combat', 12)
    self.set_skill('hacking', 15)
    self.maxpsy = 25
    self.maxap = 5
    self.cost = 0
    game.add_merc(self)
