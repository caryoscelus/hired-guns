##
##  Copyright (C) 2016 caryoscelus
##
##  This file is part of HiredGuns
##  https://github.com/caryoscelus/hired-guns/
##  
##  This program is free software: you can redistribute it and/or modify
##  it under the terms of the GNU General Public License as published by
##  the Free Software Foundation, either version 3 of the License, or
##  (at your option) any later version.
##  
##  This program is distributed in the hope that it will be useful,
##  but WITHOUT ANY WARRANTY; without even the implied warranty of
##  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
##  GNU General Public License for more details.
##  
##  You should have received a copy of the GNU General Public License
##  along with this program.  If not, see <http://www.gnu.org/licenses/>.
##

"""Generic parts of advanced menu"""

from collections import OrderedDict

class Outcome(object):
    """Outcome for multi-outcome advanced menu"""
    def __init__(self):
        self.condition = None
    
    def set_result(self):
        """Implement this to store outcome result to be used in launch.
        
        Can accept any number of args or kwargs - they are passed unchanged
        """
        pass
    
    def launch(self):
        """This is called when outcome happens. Implement in your subclass."""
        pass

class LabelOutcome(Outcome):
    """Outcome storing a simple label"""
    def __init__(self):
        super(LabelOutcome, self).__init__()
        self.label = None
    
    def set_result(self, label):
        self.label = label

class AdvancedMenuOption(object):
    def __init__(self):
        super(AdvancedMenuOption, self).__init__()
        self.requires = list()
    
    def can_do(self):
        return all([req.check() for req in self.requires])
    
    def pay_costs(self):
        for req in self.requires:
            req.pay()

class OutcomeAdvancedMenuOption(AdvancedMenuOption):
    """AdvancedMenuOption supporting various outcomes
    """
    
    """Which class to use for outcome storage."""
    outcome_class = Outcome
    
    def __init__(self):
        super(OutcomeAdvancedMenuOption, self).__init__()
        self.outcomes = OrderedDict()
        self.forced_conditions = OrderedDict()
    
    def force_outcome(self, name, condition):
        self.forced_conditions[name] = condition
    
    def outcome_condition(self, name, condition):
        if not name in self.outcomes:
            self.outcomes[name] = self.outcome_class()
        self.outcomes[name].condition = condition
    
    def outcome_result(self, name, *args, **kwargs):
        if not name in self.outcomes:
            self.outcomes[name] = self.outcome_class()
        self.outcomes[name].set_result(*args, **kwargs)

class APIAdvancedMenuOption(AdvancedMenuOption):
    """AdvancedMenuOption that automatically generates api.
    
    Inherit this and put list of Requirement classes into api_classes and
    you'll get automatic api for adding requirements, based on
    Requirement.api_name or __name__
    """
    
    api_classes = list()
    
    def __getattr__(self, name):
        for cl in self.api_classes:
            api_name = getattr(cl, 'api_name', cl.__name__)
            if api_name == name:
                def f(*args, **kwargs):
                    self.requires.append(cl(*args, **kwargs))
                return f
        raise AttributeError('no such attribute or api class: {}'.format(name))

class Requirement(object):
    def check(self):
        return False
    
    def pay(self):
        pass

class AdvancedMenu(object):
    def __init__(self, option_class):
        super(AdvancedMenu, self).__init__()
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
