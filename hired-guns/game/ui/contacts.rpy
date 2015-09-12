screen contacts:
    tag main_view
    vbox:
        text "Contacts"
        ypos STATUS_PANEL_HEIGHT
        viewport:
            draggable True
            mousewheel True
            scrollbars 'vertical'
            vbox:
                for contact in world.pc.contacts:
                    if contact.type != 'unknown':
                        add contact.target.image zoom 0.333
                    text contact.name
                    if contact.type == 'merc':
                        textbutton "Hire"
                    textbutton "Call"
