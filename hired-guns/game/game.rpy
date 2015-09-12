init -10 python:
    class Game(object):
        def __init__(self):
            self.mercs = list()
        
        def add_merc(self, merc):
            self.mercs.append(merc)
    
    game = Game()
