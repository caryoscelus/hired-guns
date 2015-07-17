label test_mission(mission):
    "mission [mission.name] start"
    call choose_mercs_for_mission(mission)
    "There are some angry monsters waiting to eat you!"
    $ monsters = True
label monster_loop:
    $ merc = random_merc()
    $ merc.hurt(1)
    "[merc.name] was hurt!"
    merc.speaker "I am hurt!"
    selected_merc().speaker "Aww..."
    menu:
        "What are we gonna do?"
        "Pacify them\
                ^^selected_merc().has_trait('pacifist')":
            $ pacifist = selected_merc()
            pacifist.speaker "Nya! Nya! Nya!!!"
            call screen roll_dices(4)
            if len([x for x in _return if x > 3]) >= 2:
                $ monsters = False
                "Monsters were scared by [pacifist.name]'s strange rite of pacifying and flew away"
            else:
                "Monsters observe [pacifist.name]'s rite curiously."
        "Kill everything!\
                ^^not selected_merc().has_trait('pacifist')":
            selected_merc().speaker "Burn with fire, monsters!"
            $ monsters = False
            $ affect_trait('pacifist', -10)
        "Sneak out of this ambush!\
                ^^selected_merc().has_skill('stealth')":
            $ merc = selected_merc()
            merc.speaker "Shhhhh...."
            "Sneak, sneak, sneak!"
            call screen roll_dices(merc.get_skill('stealth'))
            if 6 in _return:
                $ monsters = False
                "We snuck out!"
            elif 5 in _return:
                "We thought we snuck out, but after a minute or two, monsters appeared again!"
            else:
                "Monsters easily tracked us and ambushed again.."
    if monsters:
        jump monster_loop
    return


label test_gfx_mission(mission):
    $ vn_mode('nvl')
    "Hello"
    "la-la-la"
    $ vn_mode('adv')
    return
