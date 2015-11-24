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
            has vbox
            grid w h:
                xfill True
                for y in range(h):
                    for x in range(w):
                        frame:
                            ysize 120
                            use battle_cell(manager, x, y)
            button:
                text "End Turn!"
                action Function(manager.end_turn)
    textbutton "Force quit" yalign 1.0 action Return()

screen battle_cell(manager, x, y):
    $ turnman = manager.turnman
    $ field = turnman.world
    $ merc = field.grid[y][x].get()
    button action Function(manager.clicked, field.sides['pc'], (x, y)):
        has vbox
        hbox:
            text "[x]:[y]"
            if merc:
                text "[merc.name]" bold (merc is manager.selected)
        if merc:
            hbox:
                add merc.image zoom 0.25

label test_battle:
    show screen debug_all(world, _layer='debug')
    $ battle = HGBattle(Turnman, world)
    $ battle.add_enemy(Monster('low monster'))
    $ start_battle(battle)
    return
