screen contacts:
    tag main_view
    frame ypos STATUS_PANEL_HEIGHT xfill True yfill True:
        has vbox
        text "Contacts"
        viewport:
            draggable True
            mousewheel True
            scrollbars 'vertical'
            vbox:
                for contact in world.pc.contacts:
                    hbox:
                        vbox:
                            if contact.type != 'unknown':
                                add contact.target.image zoom 0.333
                            text contact.name
                        vbox:
                            text "Here goes non-existant contact description.."
                            hbox:
                                if contact.type == 'merc':
                                    textbutton "Hire" action Function(world.pc.employ, contact.target)
                                textbutton "Call"
