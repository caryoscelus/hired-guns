    #@ENTRY
    #@ID:25d00d08-bcda-4c53-a320-7ebf7b21f790
    #@LABEL:encounter_lone_guard
label encounter_lone_guard:
    "There is a guard in the corridor."

    menu:
        "What do we do, commander?"
        "Play with his mind to convince him that you are not the intruders he is waiting for.^^\
            require_skill('telepathy', 1);\
            force_outcome('success', True);\
            outcome_label('success', 'cheese_search_for_datajack');\
            ":
            pass

    return


