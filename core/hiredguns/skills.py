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
from dracykeiton.translate import _
from dracykeiton.entity import Entity, mod_dep, properties

KNOWN_SKILLS = dict(
    resilience  = _("Resilience"),
    dexterity   = _("Dexterity"),
    strength    = _("Strength"),
    mind        = _("Mind"),
    speed       = _("Speed"),
    
    telepathy   = _("Telepathy"),
    hacking     = _("Hacking"),
    
    mechanics   = _("Mechanics"),
    cooking     = _("Cooking"),
    
    stealth     = _("Stealth"),
    detection   = _("Detection"),
    
    unarmed     = _("Unarmed combat"),
    knives      = _("Knife combat"),
    
    firearms    = _("Firearms"),
    sniping     = _("Sniping"),
    explosives  = _("Explosives"),
)

@properties(skills=list)
class Skills(Entity):
    @unbound
    def has_skill(self, skill, level=1):
        return skill in self.skills and getattr(self, skill, 0) >= level
    
    @unbound
    def set_skill(self, skill, level):
        if not skill in self.skills:
            raise ValueError('{} is not skill'.format(skill))
        setattr(self, skill, level)
    
    @unbound
    def set_skills(self, **skills):
        for skill, value in skills.items():
            self.set_skill(skill, value)
    
    @unbound
    def get_skill(self, skill):
        if not skill in self.skills:
            raise ValueError('{} is not skill'.format(skill))
        return getattr(self, skill)
    
    @unbound
    def change_skill(self, skill, amount):
        real_value = 2**self.get_skill(skill) + amount
        value = log(real_value, 2)
        self.set_skill(skill, value)

def skill(cl):
    if not isinstance(cl, type):
        if isinstance(cl, str):
            class _cl(Entity):
                pass
            _cl.__name__ = cl
            cl = _cl
        else:
            raise TypeError('skill called with an arguments {} which is neither class nor string'.format(cl))
    skill_name = cl.__name__
    old_init = cl.__dict__.get('_init')
    @unbound
    def new_init(self, *args, **kwargs):
        self.skills.append(skill_name)
        if old_init:
            old_init(self, *args, **kwargs)
    cl._init = new_init
    cl = properties(**{cl.__name__:0})(cl)
    return mod_dep(Skills)(cl)

@mod_dep(*[skill(s) for s in KNOWN_SKILLS])
class HGSkills(Entity):
    pass

@mod_dep(Skills)
@properties(skill_progression=dict)
class SkillsProgress(Entity):
    @unbound
    def set_priority(self, skill, amount):
        self.skill_progression[skill] = amount
    
    @unbound
    def progress_skills(self, xp):
        for skill in self.skills:
            priority = self.skill_progression and self.skill_progression.get(skill, 0) or 1 / len(self.skills)
            self.change_skill(priority*xp)
