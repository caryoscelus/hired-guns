# skip main menu
label main_menu:
    return

# import our modules
init python:
    from hiredguns.world import HiredGunsWorld

# starting here
label start:
    $ world = HiredGunsWorld()
    show screen debug_all(world)
    "YOU ARE A HIRED GUN. ONE DAY YOU'RE GONNA DIE FOR A FEW COINS.."
    ".."
    "YOU DIED FOR A FEW COINS. HOW UNLUCKY."
    return
