screen Travel(travel_target=None):
    default target = travel_target
    tag main_view
    vbox:
        ypos STATUS_PANEL_HEIGHT
        text "Travel"
        for place in world.places:
            text place.name
            textbutton "Buy ticket"
