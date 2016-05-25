init python:
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
    frame yfill True:
        xmargin 0 ymargin 0 xpadding 0 ypadding 0
        has vbox
        grid w h:
            xfill True
            for y in range(h):
                for x in range(w):
                    frame:
                        xmargin 0 ymargin 0 xpadding 0 ypadding 0
                        ysize 160
                        use battle_cell(manager, x, y, possible_actions)
        hbox:
            textbutton "End turn":
                action Function(manager.end_turn)
            # TODO: customizeable
            key 'K_RETURN' action Function(manager.end_turn)
            if manager.can_finish():
                textbutton "Finish encounter":
                    action [Function(manager.end_encounter), Return()]
                key 'q' action [Function(manager.end_encounter), Return()]
    textbutton "Force quit" yalign 1.0 action Return()
    key 'Q' action Return()

screen battle_cell(manager, x, y, possible_actions):
    python:
        turnman = manager.turnman
        field = turnman.world
        cell = field.grid[y][x]
        merc = cell.get()
        selected = manager.selected
        side = field.sides['pc']
        possible_actions = [action for action in possible_actions if action.check_action(selected)]
        if merc:
            mode = 'self' if merc.ally_group == 'pc' else 'invisible'
    button:
        xpadding 0 ypadding 0
        xfill True yfill True
        background (merc and merc is manager.selected and "#bbf" or "#fff")
        
        action Function(manager.clicked, side, (x, y))
        hovered Function(manager.hovered, side, (x, y))
        
        textbutton merc and merc.name or '':
            background None
            xmargin 0 ymargin 0
            xpadding 0 ypadding 0
            text_hover_bold True
            if merc:
                action Show('unit_description', unit=merc, mode=mode)
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
                xpos 130 ypos 40 xsize 120 ysize 108
                has vbox
                textbutton "<nothing>":
                    action Function(manager.clicked_inventory, merc, None) text_bold (None is merc.wielded) text_size 18
                for item in merc.inv:
                    textbutton "[item.name]":
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

label test_battle:
    show screen debug_all(world, _layer='debug')
    python:
        world.pc.put_to_inv(Gun())
        world.pc.employ(game.mercs_named['nya'])
        world.pc.employ(game.mercs_named['madninja'])
        game.mercs_named['nya'].put_to_inv(Gun())
        game.mercs_named['nya'].put_to_inv(SniperRifle())
        battle = HGBattle(Turnman, world)
        battle.add_enemy(Monster('low monster'))
        battle.add_enemy(Monster('low monster'))
        battle.add_enemy(Monster('low monster'))
        start_battle(battle)
    return
