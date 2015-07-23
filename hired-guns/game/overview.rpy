screen cash_view(merc):
    frame:
        has vbox
        text "You have {} of moneys.".format(merc.money)

screen reputation_view(world):
    frame:
        has vbox
        text "You have reputation.."

screen mission_choice_view(world, state):
    frame:
        has vbox
        text "You have missions"
        for mission in world.missions:
            textbutton mission.name action [SetField(world, 'active_mission', mission), SetDict(state, 'state', 'mission')]

screen mission_details_view(world):
    frame:
        has vbox
        text "You have mission details"

screen buy_equipment(world):
    frame:
        has vbox
        text "You buy equipment"

screen hire_mercs_new(world):
    frame:
        has vbox
        text "You hire mercs"

screen overview(world):
    default state = {'state':'overview'}
    vbox:
        xalign 0.5 yalign 0.5
        hbox:
            use cash_view(world.pc)
            use reputation_view(world)
            vbox:
                if state['state'] != 'overview':
                    textbutton "<- Back" action SetDict(state, 'state', 'overview')
                if state['state'] == 'overview':
                    use mission_choice_view(world, state)
                elif state['state'] == 'mission':
                    use mission_details_view(world)
                elif state['state'] == 'equip':
                    use buy_equipment(world)
                elif state['state'] == 'hire':
                    use hire_mercs_new(world)
                else:
                    $ raise ValueError('unknown state {}'.format(state))
        hbox:
            textbutton "Hire mercs" action SetDict(state, 'state', 'hire')
            textbutton "Buy equipment" action SetDict(state, 'state', 'equip')
            textbutton "Start mission"
