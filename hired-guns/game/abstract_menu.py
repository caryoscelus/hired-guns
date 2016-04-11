# generic parts of advanced menu

class AdvancedMenu(object):
    def __init__(self, option_class):
        self.option_class = option_class
        self.caption = None
        self.options = list()
        self.active_option = None
    
    def __getattr__(self, name):
        return getattr(self.active_option, name)
    
    def start(self, caption):
        self.caption = caption
        self.options = list()
        self.active_option = None
    
    def option(self, name):
        self.active_option = self.option_class(name)
        self.options.append(self.active_option)
    
    def launch(self):
        pass
