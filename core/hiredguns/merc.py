##
##  Copyright (C) 2015 caryoscelus
##
##  This file is part of HiredGuns
##  https://bitbucket.org/caryoscelus/hired-guns/
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

"""Merc"""

from dracykeiton.compat import *
from dracykeiton.entity import Entity, mod_dep, simplenode, depends, listener
from .nation import Nation
from .traits import Traits, TraitAttitude, Attitude
from .skills import Skills
from .monster import Monster
from .contacts import Contacts
from .time import Time

MERC_STATUSES = ('free', 'busy', 'injured', 'dead')
class MercStatus(Entity):
    """Status of merc for in-between mission display."""
    @unbound
    def _init(self, status='free'):
        self.dynamic_property('merc_status', status)
        self.check_merc_status()(self, status)
    
    @unbound
    def _load(self):
        self.add_set_node('merc_status', self.check_merc_status())
    
    @simplenode
    def check_merc_status(value):
        if value in MERC_STATUSES:
            return value
        raise ValueError('there is no such merc as status as {}.. sorry'.format(value))

@mod_dep(Attitude)
class Hire(Entity):
    @unbound
    def _init(self, cost=0):
        self.dynamic_property('cost', cost)
    
    @unbound
    def hire(self, mission):
        if self.attitude < 0:
            return False
        return True

class Money(Entity):
    @unbound
    def _init(self):
        self.dynamic_property('money', 0)
    
    @unbound
    def pay(self, amount):
        self.money -= amount
    
    @unbound
    def spend_money(self, amount):
        if amount <= self.money:
            self.money -= amount
            return True
        return False

@mod_dep(Money)
class Employ(Entity):
    @unbound
    def _init(self):
        self.dynamic_property('team', list())
    
    @unbound
    def employ(self, other):
        if other in self.team:
            return
        if self.spend_money(other.cost):
            self.team.append(other)
            other.be_born()
    
    @unbound
    def unemploy(self, other):
        self.team.remove(other)

@mod_dep(Money)
class Tickets(Entity):
    @unbound
    def _init(self):
        self.dynamic_property('tickets', dict())
    
    @unbound
    def buy_ticket(self, place, time):
        # TODO: real tickets
        if self.spend_money(place.ticket_price):
            if not time.t in self.tickets:
                self.tickets[time.t] = list()
            self.tickets[time.t].append(place)
    
    @unbound
    def get_tickets_on(self, time):
        return self.tickets.get(time.t, list())
    
    @unbound
    def has_ticket_for(self, place):
        return place in self.tickets.values()
    
    @unbound
    def next_ticket_to(self, place):
        tickets_to = [
            t
                for t in self.tickets
                    if self.tickets[t] is place
        ]
        return Time(min(tickets_to))
    
    @unbound
    def cleanup_tickets(self, time):
        self.tickets = {
            t : self.tickets[t]
                for t in self.tickets
                    if t >= time.t
        }

class Preferences(Entity):
    """Describes where mercs prefers to go, what to use, etc"""
    @unbound
    def _init(self):
        self.dynamic_property('preferences', dict())
    
    @unbound
    def add_preference(self, pref, value):
        self.preferences[pref] = value
    
    @unbound
    def choose(self, pref_list):
        """Choose from given list.
        
        For now, it chooses option with highest preference according to sorted.
        I.e. when there are few equally highest values, one will be chosen based on results of 'sorted'.
        TODO: use proper random instead.
        """
        prefs = {
            pref : self.preferences.get(pref, 0)
                for pref in pref_list
        }
        return sorted(prefs, key=prefs.get)[-1]

@mod_dep(
    # basic battle stuff
    Monster,
    
    # merc stuff
    Nation,
    MercStatus,
    Traits,
    Skills,
    TraitAttitude,
    Hire,
    Employ,
    Money,
    Contacts,
    Tickets,
    Preferences,
)
class Merc(Entity):
    """Main mercenary class"""
    @unbound
    def _init(self, id='merc'):
        self.id = id
        self.maxhp = 5
