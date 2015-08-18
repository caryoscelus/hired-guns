label test_mission(mission):
    $ push_mode('nvl', left=40, right=620)
    nvl clear
    "mission [mission.name] start"
    show jungle00:
        xalign 0.9 yalign 0.2
        zoom 0.2
    "There are some angry monsters waiting to eat you!"
    $ define_var('monsters', True)
label monsters_loop:
    $ define_var('merc', random_merc())
    $ merc.hurt(1)
    "[merc.name] was hurt!"
    merc.speaker "I am hurt!"
    selected_merc().speaker "Aww..."
    $ random_encounter(level=(2, 6))
    menu:
        "What are we gonna do?"
        "Pacify them^^\
            psy_cost(10);\
            roll(4);\
            require_trait('pacifist');\
            outcome_condition('success', get_dice((4, 6), atleast=2));\
            outcome_label('success', 'monsters_pacified');\
            outcome_label('failure', 'monsters_not_pacified');\
            ":
            pass
        "Kill everything!^^\
            money_cost(10);\
            force_outcome('success', get_team_skill('unarmed_combat') >= 6);\
            roll(3);\
            require_skill('unarmed_combat', 3, 'sum');\
            outcome_condition('success', get_dice((3, 6), atleast=1));\
            outcome_label('success', 'monsters_killed');\
            outcome_label('failure', 'monsters_not_killed');\
            affect_trait('pacifist', -10);\
            ":
            pass
        "Sneak out of this ambush!^^\
            force_outcome('success', selected_merc().get_skill('stealth') >= 6);\
            roll(selected_merc().get_skill('stealth'));\
            require_skill('stealth', 3);\
            outcome_condition('success', get_dice((4, 6), atleast=3));\
            outcome_label('success', 'snuck_out');\
            outcome_label('failure', 'not_snuck_out');\
            ":
            pass
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

label snuck_out:
    $ monsters = False
    nvl clear
    "We snuk out"
    return

label not_snuck_out:
    nvl clear
    "We haven't snuk out"
    return

label monsters_end:
    "And thus we continue our journey"
    $ pop_mode()
    "We finished the mission! Yay!"
    $ mission_outcome('success')
    return


label test_gfx_mission(mission):
    $ push_mode('nvl', left=200)
    nvl clear
    "So you're on a mission"
    $ roll_skill_hurt('stealth', (3, 6), atleast=1, damage=3)
    "Now do something!!"
    $ random_encounter(with_tags={'random'})
    "Now battle!"
    $ battle = HGBattle(Turnman, world)
    $ battle.add_enemy(Monster('low monster'))
    $ start_battle(battle)
    "Mission ends here"
    $ mission_outcome('success')
    nvl clear
    $ pop_mode()
    return
