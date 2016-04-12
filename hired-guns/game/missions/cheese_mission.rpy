    #@ENTRY
    #@ID:971dda3a-de1b-4608-878a-7b928a7bce78
    #@LABEL:Mission beginning
label cheese_mission(mission):
    $ push_mode('nvl', None)
    $ define_var('stealth_penalty', 0)
    $ define_var('time_left', 30)
    $ world.pc.set_skill('unarmed', 2)
    nvl clear
    "Your team will be smuggled into the infernal Cheese-Making station inside dairy freighter, concealed inside half-empty milk canisters. You have to choose the method of entrance."
    menu:
        "Your choice, commander."
        "Ambush milk transporting workers and seize their uniforms^^\
            roll(get_team_skill('unarmed_combat'));\
            require_skill('unarmed', 4);\
            outcome_condition('success', get_dice((4, 6), atleast=3));\
            outcome_result('success', 'cheese_seize_ok');\
            outcome_result('failure', 'cheese_seize_fail');\
             ":
            pass


        "Sneak inside the cheese manufacture facility via toxic dump removal plumbing system":
            $ roll_skill_hurt('resilience', (4, 6), atleast=2, damage=3)
            call cheese_toxic_sneak


        "Attack facility guards head-on":
            $ roll_skill_hurt('resilience', (4, 6), atleast=2, damage=3)

    jump cheese_entered







    #@ENTRY
    #@ID:f0719c78-a671-43b5-864f-15647f99260c
    #@LABEL:cheese_seize_fail
    #@PARENT:971dda3a-de1b-4608-878a-7b928a7bce78
label cheese_seize_fail:

    nvl clear
    "That... Didn't quite work out. Workers threw up quite a fight, and you attracted some unwanted attention."
    "Attempts to act stealthily are going to be difficult now."
    $ stealth_penalty += 2 
    $ time_left -= 5
    return












    #@ENTRY
    #@ID:95a386bb-889b-4bdd-b9b6-b822153ebe58
    #@LABEL:cheese_seize_ok
    #@PARENT:971dda3a-de1b-4608-878a-7b928a7bce78
label cheese_seize_ok:

    nvl clear
    "They never saw you coming. Having obtained worker uniform, you are all set to blend in."
    $ stealth_penalty -= 1 
    return













    #@ENTRY
    #@ID:4f9d692e-42ec-43e8-83c8-e20a04eb4a74
    #@LABEL:cheese_toxic_sneak
    #@PARENT:971dda3a-de1b-4608-878a-7b928a7bce78
label cheese_toxic_sneak:

    nvl clear
    "Crawling through toxic waste never is a very pleasant experience."
    return



    #@ENTRY
    #@ID:252f57cc-099b-429d-992a-c41f0eaea11f
    #@LABEL:cheese_entered
label cheese_entered:
    nvl clear
    "You are inside. It's only a mtter of time before your intrusion is detected and a full-scale hunter-seeker response unit is deployed."
    "Approximate time till detection: [time_left]."
    menu:
        "What is our next step, commander?"
        "Search for a datajack to gain access into the system^^\
            require_skill('hacking', 2);\
            force_outcome('success', True);\
            outcome_result('success', 'cheese_search_for_datajack');\
            ":
            pass



    #@ENTRY
    #@ID:b15e3a7f-d644-4789-b817-0f29f78c0f32
    #@LABEL:cheese_search_for_datajack
    #@PARENT:252f57cc-099b-429d-992a-c41f0eaea11f
label cheese_search_for_datajack:
    nvl clear
    "Uh-oh, here comes the trouble"


