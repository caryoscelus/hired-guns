screen overview_new:
    tag main_view
    vbox:
        ypos STATUS_PANEL_HEIGHT
        text "Overview"
        hbox:
            text "It's {} now".format(world.time)
            textbutton "Pass a day" action Function(world.pass_day)
        text "You are on {}".format(world.now_place.name)
        if world.active_mission:
            text "You are on {} mission".format(world.active_mission.name)
        else:
            text "You are not on a mission"
