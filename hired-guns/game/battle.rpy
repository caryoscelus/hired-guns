init python:
    from dracykeiton.proxyentity import ProxyEntity

screen battle(manager):
    if manager:
        $ turnman = manager.turnman
        frame:
            has vbox
            grid 2 1:
                xfill True
                frame:
                    xalign 0.0
                    has vbox
                    label "left"
                    use battle_side(manager, turnman.world.sides['pc'])
                frame:
                    xalign 1.0
                    has vbox
                    label "right"
                    use battle_side(manager, turnman.world.sides['enemy'])
            button:
                text "Roll!"
    textbutton "Force quit" yalign 1.0 action Return()

screen battle_side(manager, side):
    default proxies = {}
    frame:
        has vbox
        for entity in side.members:
            if not entity in proxies:
                $ proxy = ProxyEntity(entity)
                $ proxies[entity] = proxy
            else:
                $ proxy = proxies[entity]
            button:
                hbox:
                    if proxy.image:
                        add proxy.image zoom 0.333
                    vbox:
                        text proxy.name bold (proxy == manager.selected)
                        hbox:
                            $ strategies = manager.get_strategies(proxy)
                            for strategy in strategies:
                                $ f = manager.set_strategy(side, proxy, strategy)
                                if action:
                                    $ f = Function(f)
                                button:
                                    text strategy.name
                                    action f
                        text "target: {}".format(proxy.target)
                        hbox:
                            add EntityText(proxy, "hp {0.hp:.0f}/{0.maxhp:.0f}")
                            bar value EntityValue(proxy, 'hp', proxy.maxhp)
                
                action Function(manager.clicked, side, proxy)
