init python:
    from dracykeiton.entity import mod_dep, ProxyEntity, InterpolatingCache
    from dracykeiton.action import get_actions
    from hiredguns.combat import Gun
    
    @mod_dep(InterpolatingCache)
    class ProxyMonster(ProxyEntity):
        pass

screen battle(manager):
    if manager:
        python:
            turnman = manager.turnman
            field = turnman.world
            w, h = field.size
            selected = manager.selected
            possible_actions = [name for name in get_actions(selected) if getattr(selected, 'check_'+name)(ignore_target=True)]
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
            button:
                text "End Turn!"
                action Function(manager.end_turn)
    textbutton "Force quit" yalign 1.0 action Return()

screen battle_cell(manager, x, y, possible_actions):
    python:
        turnman = manager.turnman
        field = turnman.world
        cell = field.grid[y][x]
        merc = cell.get()
        selected = manager.selected
        possible_actions = [name for name in possible_actions if getattr(selected, 'check_'+name)(target=cell)]
        side = field.sides['pc']
    button:
        xpadding 0 ypadding 0
        xfill True yfill True
        action Function(manager.clicked, side, (x, y))
        hovered Function(manager.hovered, side, (x, y))
        if merc:
            vbox:
                hbox:
                    add (merc.image or 'unknown') zoom 0.25
                    vbox:
                        text "inv"
                        for item in merc.inv:
                            textbutton "[item.name]" action Function(manager.clicked_inventory, merc, item) text_bold (item is merc.wielded)
                hbox:
                    vbox:
                        text "ap [merc.ap] / [merc.maxap]" size 12
                        text "hp [merc.hp] / [merc.maxhp]" size 12
                    if selected and selected.aim_target == cell:
                        vbox:
                            text "hit chance [selected.hit_chance]" size 12
                            text "hit damage [selected.hit_damage]" size 12
        vbox:
            hbox:
                text "[x]:[y]"
                if merc:
                    text "[merc.name]" bold (merc is manager.selected)
            hbox:
                for name in possible_actions:
                    textbutton "[name]":
                        action Function(manager.clicked_action, name)

label test_battle:
    show screen debug_all(world, _layer='debug')
    python:
        world.pc.put_to_inv(Gun())
        world.pc.employ(game.mercs_named['nya'])
        world.pc.employ(game.mercs_named['madninja'])
        battle = HGBattle(Turnman, world)
        battle.add_enemy(Monster('low monster'))
        battle.add_enemy(Monster('low monster'))
        battle.add_enemy(Monster('low monster'))
        start_battle(battle)
    return
