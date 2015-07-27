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
        
        init_world()
        world.pc.money = 115
        test_mission = Mission('test mission', 'test_mission', payment=30)
        test_mission.description = """
            {p}This is just a test mission in a jungle.
            {p}la-la-la
        """
        test_mission.tags.update(set({'test', 'jungle'}))
        world.add_mission(test_mission)
        world.add_mission(Mission('test gfx mission', 'test_gfx_mission', payment=10))
        world.add_mission(Mission('cheese mission', 'cheese_mission', payment=20))
        
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
        
        world.mercs.append(Merc('nobody'))
        
        pacifist = Merc('pacifist')
        pacifist.add_trait('pacifist')
        pacifist.set_skill('stealth', 4)
        pacifist.maxpsy = 15
        pacifist.cost = 10
        world.mercs.append(pacifist)
        
        ninja = Merc('ninja')
        ninja.set_skill('stealth', 7)
        ninja.set_skill('unarmed_combat', 2)
        ninja.cost = 20
        world.mercs.append(ninja)
        
        brute = Merc('brute')
        brute.set_skill('unarmed_combat', 5)
        brute.cost = 15
        world.mercs.append(brute)
    $ renpy.show_screen('debug_all', world, _layer='debug')
    #"YOU ARE A HIRED GUN. ONE DAY YOU'RE GONNA DIE FOR A FEW COINS.."
label loop:
    scene white
    $ world.update_missions()
    call screen overview(world)
    jump loop
    "YOU DIED FOR A FEW COINS. HOW UNLUCKY."
    return
