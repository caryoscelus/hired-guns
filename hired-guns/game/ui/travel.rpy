screen travel(travel_target=None):
    default target = travel_target
    tag main_view
    hbox:
        ypos STATUS_PANEL_HEIGHT
        vbox:
            text "Travel to"
            viewport:
                xfill False
                draggable True
                mousewheel True
                scrollbars 'vertical'
                vbox:
                    for place in world.places:
                        button action SetScreenVariable('target', place):
                            has vbox
                            text place.name
        vbox:
            if target is None:
                text "Select place to see its description and/or buy tickets"
            else:
                text target.name
                vbox:
                    textbutton "Buy ticket" action Function(world.pc.buy_ticket, target, world.time)
                    if target in world.pc.get_tickets_on(world.time):
                        textbutton "Go!" action Function(world.goto, target)
                    elif world.pc.has_ticket_for(target):
                        textbutton "Pass time until ticket" action Function(world, pass_time_until, world.pc.next_ticket_to(target))
