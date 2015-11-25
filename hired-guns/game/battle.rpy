init python:
    from dracykeiton.entity import mod_dep
    from dracykeiton.proxyentity import ProxyEntity
    from dracykeiton.interpolate import InterpolatingCache
    
    @mod_dep(InterpolatingCache)
    class ProxyMonster(ProxyEntity):
        pass

screen battle(manager):
    if manager:
        $ turnman = manager.turnman
        $ field = turnman.world
        $ w, h = field.size
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
                            use battle_cell(manager, x, y)
            button:
                text "End Turn!"
                action Function(manager.end_turn)
    textbutton "Force quit" yalign 1.0 action Return()

screen battle_cell(manager, x, y):
    $ turnman = manager.turnman
    $ field = turnman.world
    $ merc = field.grid[y][x].get()
    button:
        xpadding 0 ypadding 0
        xfill True yfill True
        action Function(manager.clicked, field.sides['pc'], (x, y))
        if merc:
            vbox:
                hbox:
                    add (merc.image or 'unknown') zoom 0.25
                text "ap [merc.ap] / [merc.maxap]" size 12
                text "hp [merc.hp] / [merc.maxhp]" size 12
        hbox:
            text "[x]:[y]"
            if merc:
                text "[merc.name]" bold (merc is manager.selected)

label test_battle:
    show screen debug_all(world, _layer='debug')
    $ world.pc.employ(game.mercs_named['nya'])
    $ world.pc.employ(game.mercs_named['madninja'])
    $ battle = HGBattle(Turnman, world)
    $ battle.add_enemy(Monster('low monster'))
    $ battle.add_enemy(Monster('low monster'))
    $ battle.add_enemy(Monster('low monster'))
    $ start_battle(battle)
    return
