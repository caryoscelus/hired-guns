﻿# skip main menu
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
        world.add_mission(Mission('test mission', 'test_mission'))
        world.add_mission(Mission('test gfx mission', 'test_gfx_mission'))
        
        world.mercs.append(Merc('nobody'))
        
        pacifist = Merc('pacifist')
        pacifist.add_trait('pacifist')
        world.mercs.append(pacifist)
        
        ninja = Merc('ninja')
        ninja.set_skill('stealth', 5)
        world.mercs.append(ninja)
    show screen debug_all(world)
    "YOU ARE A HIRED GUN. ONE DAY YOU'RE GONNA DIE FOR A FEW COINS.."
label loop:
    "YOU'VE BEEN SUCKED INTO ETERNAL LOOP."
    jump loop
    "YOU DIED FOR A FEW COINS. HOW UNLUCKY."
    return
