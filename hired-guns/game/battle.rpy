init python:
    from dracykeiton.entity import mod_dep
    from dracykeiton.proxyentity import ProxyEntity
    from dracykeiton.interpolate import InterpolatingCache
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
            possible_actions = [name for name in get_actions(selected) if getattr(selected, 'check_'+name)()]
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
    button:
        xpadding 0 ypadding 0
        xfill True yfill True
        action Function(manager.clicked, field.sides['pc'], (x, y))
        if merc:
            vbox:
                hbox:
                    add (merc.image or 'unknown') zoom 0.25
                    vbox:
                        text "inv"
                        for item in merc.inv:
                            textbutton "[item.name]" action Function(merc.wield, item) text_bold (item is merc.wielded)
                hbox:
                    vbox:
                        text "ap [merc.ap] / [merc.maxap]" size 12
                        text "hp [merc.hp] / [merc.maxhp]" size 12
        vbox:
            hbox:
                text "[x]:[y]"
                if merc:
                    text "[merc.name]" bold (merc is manager.selected)
            hbox:
                for name in possible_actions:
                    textbutton "[name]":
                        hovered Function(selected.aim, cell)
                        action Function(lambda selected, name: manager.do_action(getattr(selected, name)()), selected, name)

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
