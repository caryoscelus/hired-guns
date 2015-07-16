label test_mission(mission):
    "mission [mission.name] start"
    call choose_mercs_for_mission(mission)
    $ merc = random_merc()
    $ merc.hurt(1)
    "[merc.name] was hurt!"
    merc.speaker "I am hurt!"
    selected_merc().speaker "Aww..."
    "There are some angry monsters waiting to eat you!"
    menu:
        "What are we gonna do?"
        "Pacify them\
                ^^selected_merc().has_trait('pacifist')":
            $ pacifist = selected_merc()
            pacifist.speaker "Nya! Nya! Nya!!!"
            "Monsters were scared by [pacifist.name]'s strange rite of pacifying and flew away"
        "Kill everything!\
                ^^not selected_merc().has_trait('pacifist')":
            selected_merc().speaker "Burn with fire, monsters!"
            $ affect_trait('pacifist', -10)
    return
