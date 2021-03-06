init -5 python:
    missions_to_add = list()
    
    def init_world():
        #pc_name = renpy.input(_("What is your name?"))
        pc_name = 'You'
        pc = Merc('pc')
        pc.name = pc_name
        global world
        world = HiredGunsWorld(pc)
        for mission in missions_to_add:
            world.add_mission(mission)
        for merc in game.mercs:
            world.mercs.append(merc)
            world.pc.add_contact(Contact(merc, 'merc'))
        for place in game.places.values():
            world.places.append(place)
        world.default_place = game.default_place
        world.now_place = world.default_place
    
    def roll_skill_hurt(skill, want, atleast, damage):
        renpy.call('roll_skill_hurt', skill, want, atleast, damage)
    
    def start_battle(battle):
        manager = prepare_battle(battle)
        renpy.hide_screen('team_npc_view')
        renpy.call_screen('battle', manager)
        renpy.show_screen('team_npc_view')

label roll_skill_hurt(skill, want, atleast, damage):
    $ define_var('remaining_mercs', world.active_mission.mercs.copy())
label roll_skill_hurt_loop:
    if not remaining_mercs:
        jump roll_skill_hurt_end
    $ define_var('merc', remaining_mercs.pop())
    call screen roll_dices(merc.get_skill(skill))
    $ define_var('r', [dice for dice in _return if want[0] <= dice <= want[1]])
    if len(r) < atleast:
        $ merc.hurt(damage)
    jump roll_skill_hurt_loop
label roll_skill_hurt_end:
    return
