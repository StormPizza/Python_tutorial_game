



def print_part_1(player_health, health_show,hand, hand_show,deck, deck_show, discard, discard_show):
    menu = {
        "health_show": print_health(player_health, health_show)
        "hand_show": print_hand(hand, hand_show)
        "deck_show": print_deck(deck, deck_show)
        "discard_show": print_discard(discard, discard_show)
        "room_desc_show": print_room_desc(room_desc, room_desc_show)
    }
    for show_check, stat in menu.items():
        if show_check == 0:
            stat
    for show_check, stat in menu.items():
        if show_check == 1:
            stat

    print_health(player_health, health_show)
    print_hand(hand, hand_show)
    print_deck(deck, deck_show)
    print_discard(discard, discard_show)
    print_room_desc(room_desc, room_desc_show)



def print_health(player, health_show):
    player[health] = make_two_digit(player[health])
    if health_show == 1:
        print "player health: (%s hp)" % player[health], "H " * player[health]
    else:
        print "[health](%s)" % player[health],
def print_hand(hand, hand_show):
    if health_show == 1:
        print "hand:    ", hand
    else:
        print "[hand](%s)" % hand,
def print_deck(deck, deck_show):
    print
def print_discard(discard, discard_show):
    print
def print_room_desc(room_desc, room_desc_show):
    print

def make_two_digit(number):
    number = str(number)
    if len(number) < 2:
        number = " ", number

        # Test
        # roo = {
        #     "q": toolz.pik()
        # }
        # roo["q"]
