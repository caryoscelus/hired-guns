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

init python:
    import re
    import actions_info
    import actions
    
    def menu_action(caption):
        """...
        roll(n)
        requires_skill(skill, level, who='merc'|'team')
        affects_trait(trait, amount, forbid)
        outcome_condition(name, condition)
        outcome_action(name, action)
        """
        caption, body = caption.split('^^')
        caption = caption.strip()
        body = "start_action('{}');".format(caption)+body.strip()+"finish_action();"
        expr = compile(body, '<menu_action>', 'exec')
        eval(expr, actions_info.__dict__)
        answer = actions_info.result
        actions_info.result = None
        actions.parse_results[caption] = answer
        answer['action'] = Function(eval, expr, actions.__dict__)
        return answer, caption
