# nvl screen with advanced menu
# TODO: separate menu to be usable with choice screen
screen nvl(dialogue, items=None):

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
        if items and items[0][0] == '^advanced^':
            
            vbox:
                id "menu"
                
                text am.caption style "nvl_dialogue"
                
                for option in am.options:
                    
                    button action (Function(option.launch) if option.can_do() else None):
                        has vbox

                        text option.name style "nvl_menu_choice" bold option.can_do()
                        if option.requires:
                            text "Requires:"
                            for req in option.requires:
                                text str(req) bold req.check()
        
        # regular
        elif items:
            
            vbox:
                id "menu"

                for caption, action, chosen in items:

                    if action:

                        button:
                            style "nvl_menu_choice_button"
                            action action

                            text caption style "nvl_menu_choice"

                    else:

                        text caption style "nvl_dialogue"

    add SideImage() xalign 0.0 yalign 1.0

init -1 python:
    def format_skills(skills):
        return ', '.join(['{}: {}'.format(skill[0], skill[1]) for skill in skills])
    
    def format_traits(traits):
        return ', '.join([trait for trait in traits])
