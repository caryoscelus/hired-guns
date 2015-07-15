# skip main menu
label main_menu:
    return

# starting here
label start:
    $ init_world()
    $ world.missions.append(Mission('test mission', 'test_mission'))
    show screen debug_all(world)
    "YOU ARE A HIRED GUN. ONE DAY YOU'RE GONNA DIE FOR A FEW COINS.."
label loop:
    "YOU'VE BEEN SUCKED INTO ETERNAL LOOP."
    jump loop
    "YOU DIED FOR A FEW COINS. HOW UNLUCKY."
    return
