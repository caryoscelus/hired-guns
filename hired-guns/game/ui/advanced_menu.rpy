# nvl screen with advanced menu
# TODO: separate menu to be usable with choice screen
screen nvl(dialogue, items=None):

    # TODO: fix this hack//
    if dialogue:
        $ renpy.store._current_speaker = dialogue[-1][0]

    window:
        style "nvl_window"

        has vbox:
            style "nvl_vbox"

        # Display dialogue.
        for who, what, who_id, what_id, window_id in dialogue:
            window:
                id window_id

                has hbox:
                    spacing 10

                if who is not None:
                    text who bold True # id who_id

                text what id what_id

        # Display a menu, if given.
        # advanced
        if items:
            vbox:
                id 'menu'
                
                # hacky positioning fix
                xoffset vn_mode().kwargs.get('window_xoffset', 0) + vn_mode().margins.get('left', 0)
                yoffset vn_mode().kwargs.get('window_yoffset', 0) + vn_mode().margins.get('top', 0)
                
                if items[0][0] == '^advanced^':
                    
                    text am.caption style "nvl_dialogue"
                    
                    for option in am.options:
                        
                        button action (Function(option.launch) if option.can_do() else None):
                            has vbox

                            text option.name bold option.can_do() style "nvl_dialogue"
                            if option.requires:
                                text "Requires:"
                                for req in option.requires:
                                    text str(req) bold req.check()
        
                # regular
                else:
                    
                    for caption, action, chosen in items:

                        if action:

                            button:
                                action action

                                text caption style "nvl_dialogue"

                        else:

                            text caption style "nvl_dialogue"
