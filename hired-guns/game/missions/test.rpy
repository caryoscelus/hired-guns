label test_mission(mission):
    "mission [mission.name] start"
    call choose_mercs_for_mission(mission)
    $ merc = random_merc()
    $ merc.hurt(1)
    "[merc.name] was hurt!"
    merc.speaker "I am hurt!"
    selected_merc().speaker "Aww..."
    $ affect_trait('pacifist', -10)
    return
