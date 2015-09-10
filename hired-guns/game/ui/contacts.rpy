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
                    text contact
