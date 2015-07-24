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
        text world.active_mission.name
        text "Description: {}".format(world.active_mission.description)
        text "Payment: {}".format(world.active_mission.payment)

screen buy_equipment(world):
    frame:
        has vbox
        text "You buy equipment"

init python:
    def hire_merc_new(merc, world):
        if merc in world.hired_mercs:
            world.hired_mercs.remove(merc)
        else:
            world.hired_mercs.append(merc)

screen hire_mercs_new(world):
    frame:
        has vbox
        text "Hire mercs"
        hbox:
            for merc in world.mercs:
                button style 'filled_frame' action Function(hire_merc_new, merc, world):
                    has vbox
                    text merc.name bold (merc in world.hired_mercs)
                    if merc.image:
                        add merc.image zoom 0.333

screen overview(world):
    default state = {'state':'overview'}
    vbox:
        xalign 0.5 yalign 0.5
        text "current mission: {}".format(world.active_mission and world.active_mission.name)
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
            textbutton "Start mission" action ([Function(renpy.call, 'mission', world.active_mission)] if world.active_mission else None)
