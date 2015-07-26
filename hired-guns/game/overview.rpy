screen overview_merc_list(world):
    hbox:
        for merc in world.hired_mercs:
            use merc_default(merc, None)

screen cash_view(world):
    frame:
        xsize 0.15
        ysize 0.8
        has vbox
        text "You have {} of moneys.".format(world.pc.money)
        text "After hiring mercs, {} will be left.".format(world.get_money_prediction())

screen reputation_view(world):
    frame:
        xsize 0.15
        ysize 0.8
        has vbox
        text "You have reputation.."

screen mission_choice_view(world, state):
    frame xfill True:
        has hbox
        vbox:
            text "You have missions"
            for mission in world.missions:
                textbutton mission.name action (SetField(world, 'active_mission', mission) if world.missions[mission] == 'available' else None) text_bold (mission is world.active_mission)
        if world.active_mission:
            use mission_details_view(world)

screen mission_details_view(world):
    frame xfill True:
        has vbox
        text world.active_mission.name
        text "Description: {}".format(world.active_mission.description.strip())
        text "Payment: {}".format(world.active_mission.payment)

screen buy_equipment(world):
    frame:
        has vbox
        text "You buy equipment"

label i_wont_work_with_you(merc):
    merc.speaker "I won't work with you, bastard!"
    return

init python:
    def hire_merc_new(merc, world):
        if merc.attitude < 0:
            renpy.call('i_wont_work_with_you', merc)
            return
        if merc in world.hired_mercs:
            world.hired_mercs.remove(merc)
        else:
            world.hired_mercs.append(merc)

screen hire_mercs_new(world):
    frame xfill True:
        has vbox
        text "Hire mercs"
        hbox:
            for merc in world.mercs:
                button style 'filled_frame' action Function(hire_merc_new, merc, world):
                    has vbox
                    text merc.name bold (merc in world.hired_mercs)
                    if merc.image:
                        add merc.image zoom 0.333
                    text "Costs {}".format(merc.cost)

screen overview(world):
    default state = {'state':'overview'}
    vbox:
        xalign 0.0 yalign 0.0
        text "current mission: {}".format(world.active_mission and world.active_mission.name)
        hbox:
            use cash_view(world)
            use reputation_view(world)
            vbox:
                xfill True
                hbox:
                    textbutton "Choose mission" action SetDict(state, 'state', 'overview')
                    textbutton "Hire mercs" action SetDict(state, 'state', 'hire')
                    textbutton "Buy equipment" action SetDict(state, 'state', 'equip')
                if state['state'] == 'overview':
                    use mission_choice_view(world, state)
                elif state['state'] == 'equip':
                    use buy_equipment(world)
                elif state['state'] == 'hire':
                    use hire_mercs_new(world)
                else:
                    $ raise ValueError('unknown state {}'.format(state))
        hbox:
            use overview_merc_list(world)
    textbutton "Start mission":
        xalign 1.0 yalign 1.0
        xminimum 0.2 yminimum 0.3
        action ([Function(renpy.call, 'mission', world.active_mission)] if world.active_mission and world.get_money_prediction() >= 0 else None)
