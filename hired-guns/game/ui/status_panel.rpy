define STATUS_PANEL_HEIGHT = 40

screen status_panel:
    hbox:
        xpos 0 ypos 0
        ysize STATUS_PANEL_HEIGHT
        textbutton "X"          action Hide('main_view')
        textbutton "Overview"   action Show('overview_new')
        textbutton "Contacts"   action Show('contacts')
        textbutton "Jobs"       action Show('jobs')
        textbutton "Finances"   action Show('Finances')
        textbutton "Travel"     action Show('Travel')
        text "{}".format(world.time)

screen Finances:
    tag main_view
    vbox:
        ypos STATUS_PANEL_HEIGHT
        text "Finances"
