init -10 python:
    from collections import OrderedDict
    
    class Game(object):
        def __init__(self):
            self.mercs = list()
            self.places = OrderedDict()
            self.default_place = None
        
        def add_merc(self, merc):
            self.mercs.append(merc)
        
        def add_place(self, place):
            self.places[place.id] = place
        
        def set_default_place(self, place):
            self.default_place = place
        
        def get_place(self, id):
            return self.places[id]
    
    game = Game()
