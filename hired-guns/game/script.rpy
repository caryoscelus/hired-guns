# skip main menu
label main_menu:
    return

image white = Solid('#ffffff')

# starting here
label start:
    scene white
    
    python:
        adv_menu = menu
        menu = nvl_menu
        
        init_vn_modes()
        init_world()
        world.pc.money = 4000
        world.add_mission(Mission('cheese mission', 'cheese_mission', payment=20))
        world.update_missions()
        
        world.encounter_pool.add(Encounter('encounter_test', 0, {'random', 'test'}))
        world.encounter_pool.add(Encounter('encounter_yare1', 1, {'random', 'test'}))
        world.encounter_pool.add(Encounter('encounter_yare2', 2, {'random', 'test'}))
        world.encounter_pool.add(Encounter('encounter_yare3', 3, {'random', 'test'}))
        world.encounter_pool.add(Encounter('encounter_unrand', 0, {'test'}))
        world.encounter_pool.add(Encounter('encounter_lone_guard', 1, {'indoors'}))
        
        
        world.pc.set_skill('unarmed_combat', 1)
        world.pc.set_skill('resilience', 1)
        world.pc.set_skill('hacking', 2)
        world.pc.set_skill('firearms', 1)
        world.pc.set_skill('explosives', 1)
        world.pc.set_skill('stealth', 1)
        world.pc.set_skill('telepathy', 1)
        world.pc.set_skill('mechanics', 1)
        world.pc.maxpsy = 20
    
    menu:
        "main":
            pass
        "bloody intro":
            call let_the_blood_spill
        "test battle":
            call test_battle
        "test unit description":
            call test_unit_description
        "test universal party screen":
            call test_universal_party
        "test encounter mission":
            call test_encounter_mission
    
    $ renpy.show_screen('debug_all', world, _layer='debug')
    #"YOU ARE A HIRED GUN. ONE DAY YOU'RE GONNA DIE FOR A FEW COINS.."
label loop:
    scene white
    show screen status_panel(world)
    ".."
    jump loop
    "YOU DIED FOR A FEW COINS. HOW UNLUCKY."
    return

label test_encounter_mission:
    $ world.pc.employ(game.mercs_named['brute'])
    $ world.pc.employ(game.mercs_named['pacifist'])
    call mission(world.get_mission_by_label('test_mission'))
    return
