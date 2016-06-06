##############################################################################
# Say
#
# Screen that's used to display adv-mode dialogue.
# http://www.renpy.org/doc/html/screen_special.html#say
screen say(who, what):
    window:
        id "window"

        has vbox:
            style "say_vbox"

        if who:
            text who id "who"

        text what id "what"
