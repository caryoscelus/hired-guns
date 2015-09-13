init -10 python:
    class Game(object):
        def __init__(self):
            self.mercs = list()
            self.places = list()
        
        def add_merc(self, merc):
            self.mercs.append(merc)
        
        def add_place(self, place):
            self.places.append(place)
    
    game = Game()
