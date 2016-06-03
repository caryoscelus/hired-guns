##
##  Copyright (C) 2015-2016 caryoscelus
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

from dracykeiton.compat import *

import renpy
from renpy.store import nvl, adv, Character

def apply_margins(kwargs, margins):
    if margins:
        for margin in margins:
            kwargs['window_'+margin+'_margin'] = margins[margin]

class VNMode(object):
    def __init__(self, mode, margins, **kwargs):
        self.mode = mode
        self.margins = margins or dict()
        apply_margins(kwargs, margins)
        self.kwargs = kwargs
    
    def __repr__(self):
        return 'VNMode({}, {}, **{})'.format(self.mode, self.margins, self.kwargs)

def init_vn_modes():
    renpy.store._mode_stack = [VNMode('adv', None)]

def vn_mode():
    return renpy.store._mode_stack[-1]

def push_mode(*args, **kwargs):
    renpy.store._mode_stack.append(VNMode(*args, **kwargs))

def set_window_margins(**margins):
    apply_margins(renpy.store._mode_stack[-1].kwargs, margins)

def set_window_position(x, y):
    renpy.store._mode_stack[-1].kwargs['window_xalign'] = 0
    renpy.store._mode_stack[-1].kwargs['window_yalign'] = 0
    renpy.store._mode_stack[-1].kwargs['window_xoffset'] = x
    renpy.store._mode_stack[-1].kwargs['window_yoffset'] = y

def set_text_color(color):
    renpy.store._mode_stack[-1].kwargs['what_color'] = color

def pop_mode():
    renpy.store._mode_stack.pop()

class CombinedCharacter(object):
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = dict({
            'what_prefix' : '"',
            'what_suffix' : '"',
        })
        self.kwargs.update(kwargs)
    def __call__(self, *args, **kwargs):
        kwargs_copy = self.kwargs.copy()
        kwargs_copy.update(vn_mode().kwargs)
        if vn_mode().mode == 'nvl':
            kwargs_copy['kind'] = nvl
            return Character(*self.args, **kwargs_copy)(*args, **kwargs)
        elif vn_mode().mode == 'adv':
            kwargs_copy['kind'] = adv
            return Character(*self.args, **kwargs_copy)(*args, **kwargs)
        else:
            raise ValueError('unknown mode {}'.format(_vn_mode))
