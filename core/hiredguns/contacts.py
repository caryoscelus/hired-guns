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

from dracykeiton.compat import *
from dracykeiton.entity import Entity, mod_dep, simplenode, depends, listener

CONTACT_TYPES = ('merc', 'organization', 'known', 'unknown')
class Contact(Entity):
    @unbound
    def _init(self, target=None, type='unknown'):
        self.dynamic_property('target', target)
        self.dynamic_property('type', type)
        self.dynamic_property('name', None)
    
    @unbound
    def _load(self):
        self.add_get_node('name', self.get_default_name())
    
    @depends('target', 'type')
    @simplenode
    def get_default_name(value, target, type):
        if value is None:
            if type == 'unknown':
                return 'anonymous'
            else:
                try:
                    return target.name
                except AttributeError:
                    return value
        return value

class Contacts(Entity):
    @unbound
    def _init(self):
        self.dynamic_property('contacts', list())
    
    @unbound
    def add_contact(self, contact):
        self.contacts.append(contact)
