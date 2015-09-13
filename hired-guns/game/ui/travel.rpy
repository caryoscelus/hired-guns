screen Travel(travel_target=None):
    default target = travel_target
    tag main_view
    vbox:
        ypos STATUS_PANEL_HEIGHT
        text "Travel"
        for place in world.places:
            frame:
                has vbox
                text place.name
                hbox:
                    textbutton "Buy ticket" action Function(world.pc.buy_ticket, place, world.time)
                    if place in world.pc.get_tickets_on(world.time):
                        textbutton "Go!" action Function(world.goto, place)
                    elif world.pc.has_ticket_for(place):
                        textbutton "Pass time until ticket" action Function(world, pass_time_until, world.pc.next_ticket_to(place))
