label test_mission(mission):
    $ push_mode('nvl', left=40, right=620)
    nvl clear
    "mission [mission.name] start"
    show jungle00:
        xalign 0.9 yalign 0.2
        zoom 0.2
    "There are some angry monsters waiting to eat you!"
    $ monsters = True
label monsters_loop:
    $ merc = random_merc()
    $ merc.hurt(1)
    "[merc.name] was hurt!"
    merc.speaker "I am hurt!"
    selected_merc().speaker "Aww..."
    menu:
        "What are we gonna do?"
        "Pacify them^^\
            roll(4);\
            require_trait('pacifist');\
            outcome_condition('success', get_dice((4, 6), amount=(2, 4)));\
            outcome_label('success', 'monsters_pacified');\
            outcome_label('failure', 'monsters_not_pacified');\
            ":
            pass
        "Kill everything!^^\
            roll(3);\
            outcome_condition('success', get_dice((3, 6), amount=(1, 4)));\
            outcome_label('success', 'monsters_killed');\
            outcome_label('failure', 'monsters_not_killed');\
            affect_trait('pacifist', -10);\
            ":
            pass
        #"Sneak out of this ambush!\
                #^^selected_merc().has_skill('stealth')":
            #call monsters_sneakout()
    if monsters:
        jump monsters_loop
    jump monsters_end

label monsters_killed:
    $ monsters = False
    nvl clear
    "We killed all the monsters!"
    return

label monsters_not_killed:
    nvl clear
    "Monsters were not killed."
    return

label monsters_pacified:
    $ monsters = False
    $ pacifist = selected_merc()
    nvl clear
    "Monsters were scared by [pacifist.name]'s strange rite of pacifying and flew away"
    return

label monsters_not_pacified:
    $ pacifist = selected_merc()
    nvl clear
    "Monsters observe [pacifist.name]'s rite curiously."
    return

label monsters_end:
    "And thus we continue our journey"
    $ pop_mode()
    return


label test_gfx_mission(mission):
    $ push_mode('nvl', left=200)
    nvl clear
    "So you're on a mission"
    "Now do something!!"
    "Sorry, not much can be done here.."
    nvl clear
    $ pop_mode()
    return
