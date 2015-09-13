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

DAY = 24*60*60
MONTH = 30
YEAR = 12

class Time(object):
    def __init__(self, time=0):
        self.t = time
    
    def __lt__(self, other):
        return self.t < other.t
    
    def __gt__(self, other):
        return self.t > other.t
    
    def __eq__(self, other):
        return self.t == other.t
    
    def __ne__(self, other):
        return self.t != other.t
    
    def __str__(self):
        return '{:04}-{:02}-{:02}'.format(self.year(), self.month()+1, self.day()+1)
    
    def year(self):
        return self.t // (DAY*MONTH*YEAR)
    
    def month(self):
        return self.t // (DAY*MONTH) % YEAR
    
    def day(self):
        return self.t // DAY % MONTH
    
    def pass_time(self, amount):
        self.t += amount
