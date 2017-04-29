
from settings import *
# import toolz

def get_level_type(player1, world1):
    world1.current_level += 1

    # ------------------ DEATH CHECK ( ZERO HP)
    if player1.health <= 0:
        player1.status == "dead"
        return 'death'

    # ------------------ HAND CHECK ( CANNOT MAKE FULL HAND )
    # player1.status = check_hand_min_size(player1)
    total_cards = len(player1.hand)+len(player1.deck)+len(player1.discard)
    if total_cards < 5:
        print "You do not have enough cards to make a full hand."
        print "You die from incomplete-hand syndrome"
    #     return 'dead'
    # if player1.status == "dead":
        return 'death'

    # ------------------ FINAL LEVEL CHECK
    # Limits number of levels and alerts when at final level
    if world1.current_level > world1.max_level:
        print "\n"
        return 'finished'
    elif world1.current_level == world1.max_level:
        world1.final_note = "(FINAL LEVEL)"

    # ------------------ STORE CHECK
    # world1.level_type = check_store_open(world1)
    if world1.current_level % world1.store_interval == 0:
        if world1.current_level != world1.max_level:
            world1.level_type = "we_at_store"
            # world1.level_type = "open"
            return 'store'
    else:
        world1.level_type = "we_be_fighting"


    return 'fight'
