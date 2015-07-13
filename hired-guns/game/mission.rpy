label mission(mission):
    ">> mission start"
    ">>> mission preparation phase"
    if not mission.intro is None:
        $ renpy.call(mission.intro)
    ">>> mission battle phase"
    "TEH BATTLE"
    ">>> mission outro"
    if not mission.outro is None:
        $ renpy.call(mission.outro)
    else:
        "Your mission was a failure"
    ">> mission end"
    return
