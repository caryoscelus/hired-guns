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

init python:
    from dracykeiton.compat import *
    from dracykeiton.entity import mod_dep, ProxyEntity, InterpolatingCache
    from dracykeiton.action import get_actions
    from hiredguns.combat import Gun, SniperRifle
    
    @mod_dep(InterpolatingCache)
    class ProxyMonster(ProxyEntity):
        pass

screen battle(manager):
    python:
        turnman = manager.turnman
        field = turnman.world
        w, h = field.size
        selected = manager.selected
        possible_actions = manager.get_combat_actions()
        keyman = manager.keys
    
    key 'prev_weapon' action Function(keyman.prev_weapon)
    key 'next_weapon' action Function(keyman.next_weapon)
    
    key 'prev_merc' action Function(keyman.next_merc)
    key 'next_merc' action Function(keyman.prev_merc)
    
    key 'focus_up'      action Function(keyman.active_up)
    key 'focus_down'    action Function(keyman.active_down)
    key 'focus_left'    action Function(keyman.active_left)
    key 'focus_right'   action Function(keyman.active_right)
    
    frame yfill True:
        xmargin 0 ymargin 0 xpadding 0 ypadding 0
        background None
        has vbox
        grid w h:
            xfill True
            for y in range(h):
                for x in range(w):
                    frame:
                        background None
                        xmargin 0 ymargin 0 xpadding 0 ypadding 0
                        ysize 160
                        use battle_cell(manager, x, y, possible_actions)
        hbox:
            textbutton "End turn":
                action Function(manager.end_turn)
            key 'finish_turn' action Function(manager.end_turn)
            if manager.can_finish():
                textbutton "Finish encounter":
                    action [Function(manager.end_encounter), Return()]
                key 'end_encounter' action [Function(manager.end_encounter), Return()]
    textbutton "Force quit" yalign 1.0 action Return()
    key 'force_end_encounter' action Return()

screen battle_cell(manager, x, y, possible_actions):
    python:
        turnman = manager.turnman
        field = turnman.world
        cell = field.grid[(x, y)]
        merc = cell.get()
        selected = manager.selected
        is_active = manager.active_cell == (x, y)
        side = field.sides['pc']
        possible_actions = [action for action in possible_actions if action.check_action(selected)]
        if merc:
            mode = 'self' if merc.ally_group == 'pc' else 'invisible'
    button:
        xpadding 0 ypadding 0
        xfill True yfill True
        background (merc and merc is manager.selected and "#bbf8" or None)
        
        action Function(manager.clicked, side, (x, y))
        hovered Function(manager.hovered, side, (x, y))
        
        if is_active:
            frame background '#fb06'
        
        if merc:
            textbutton merc.name or '<unknown>':
                background '#fff4'
                xmargin 0 ymargin 0
                xpadding 0 ypadding 0
                text_hover_bold True
                action Show('unit_description', unit=merc, mode=mode)
        if merc and is_active:
            key 'info' action Show('unit_description', unit=merc, mode=mode)
        add merc and (merc.image or 'unknown'):
            zoom 0.25
            xalign 0.0 yalign 1.0
        
        if merc:
            vbox:
                xalign 1.0 yalign 0.0
                xsize 128
                fixed ysize 16:
                    bar value merc.hp range merc.maxhp
                    text "hp [merc.hp] / [merc.maxhp]" size 14
                fixed ysize 16:
                    bar value merc.psy range merc.maxpsy
                    text "psy [merc.psy] / [merc.maxpsy]" size 14
        
        if merc:
            frame:
                background '#fff4'
                xpos 130 ypos 40 xsize 120 ysize 108
                has vbox
                spacing 0
                for item in manager.inventory(merc):
                    $ name = item and item.name or "<nothing>"
                    textbutton "[name]":
                        xfill True
                        action Function(manager.clicked_inventory, merc, item) text_bold (item is merc.wielded) text_size 18
        
        if merc:
            text "ap {} ({})/{}".format(merc.ap, merc.ap-merc.combat_action_ap, merc.maxap):
                xalign 1.0 yalign 1.0
                size 18
        
        if selected and selected.aim_target is cell and selected.action_mod:
            frame:
                xpos 20 ypos 40 xsize 120 ysize 50
                background "#fbb"
                has vbox
                text "[selected.action_mod.__name__]" size 16
                text "chance: {:.1f}%".format(selected.action_chance*100) size 12
                text "hit damage: {}".format(selected.hit_damage) size 12
        
        if selected and selected.aim_target is cell:
            hbox:
                xalign 0.0 yalign 1.0
                for action in possible_actions:
                    key action.__name__ action Function(manager.clicked_action, action)
                    imagebutton:
                        idle "images/ui/action.png"
                        hovered Function(manager.hovered_action, action)
                        unhovered Function(manager.unhovered_action, action)
                        action Function(manager.clicked_action, action)
                if manager.change_melee_action():
                    imagebutton:
                        idle "images/ui/action.png"
                        hovered Function(manager.hovered_melee)
                        unhovered Function(manager.unhovered_melee)
                        action Function(manager.clicked_melee)

init python:
    from hiredguns.monster import Monster
    from hiredguns.ai import DoNothing, MeleeRush
    
    @mod_dep(Monster, MeleeRush)
    class LowMonster(Entity):
        @unbound
        def _init(self):
            self.maxap = 2
            self.name = 'Low Monster'
            self.set_skill('unarmed_combat', 5)

label test_battle:
    show screen debug_all(world, _layer='debug')
    python:
        world.pc.put_to_inv(Gun())
        world.pc.employ(game.mercs_named['nya'])
        world.pc.employ(game.mercs_named['madninja'])
        game.mercs_named['nya'].put_to_inv(Gun())
        game.mercs_named['nya'].put_to_inv(SniperRifle())
        battle = new_battle()
        battle.add_enemy(LowMonster())
        battle.add_enemy(LowMonster())
        battle.add_enemy(LowMonster())
        start_battle(battle)
    return
