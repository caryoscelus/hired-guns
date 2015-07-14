# skip main menu
label main_menu:
    return

# import our modules
init python:
    from hiredguns.world import HiredGunsWorld
    from hiredguns.mission import Mission

# starting here
label start:
    $ world = HiredGunsWorld()
    $ world.missions.append(Mission('test mission', 'test_mission'))
    show screen debug_all(world)
    "YOU ARE A HIRED GUN. ONE DAY YOU'RE GONNA DIE FOR A FEW COINS.."
label loop:
    "YOU'VE BEEN SUCKED INTO ETERNAL LOOP."
    jump loop
    "YOU DIED FOR A FEW COINS. HOW UNLUCKY."
    return

label test_mission(mission):
    "mission [mission.name] start"
    call choose_mercs_for_mission(mission)
    "mission could be happening here.."
    return
