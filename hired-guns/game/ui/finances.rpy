screen finances:
    tag main_view
    frame ypos STATUS_PANEL_HEIGHT xfill True yfill True:
        has vbox
        text "Finances"
        text "{}".format(world.pc.money)
