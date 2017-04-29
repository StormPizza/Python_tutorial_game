from sys import exit
from random import randint
import enemies
import math
import time
from settings import *
import storez
# import store_instants


def transfer_random(fromlist, destlist, times):
    # transfers random cards from the FROMLIST to the DESTLIST
    for i in range(times):
        index = randint(0, len(fromlist)-1)
        destlist.append(fromlist[index])
        fromlist.remove(fromlist[index])

def dump_all(fromlist, tolist):
    transfer_random(fromlist, tolist, len(fromlist))

def starting_phase(player1, world1):
    player1.current_effects = {}  # Clears all current effects
    # Adds all passive skills to current effects
    for key, value in player1.skills_owned.items():
        if value[skilltype] == "Passive" and value[trigger] != from_hand:
            player1.add_current_effect(key)

    dump_all(player1.hand, player1.discard)
    if world1.level_type is not "we_at_store":
        player1.draw_full_hand()
    # print player1.hand

# //////////////////////////////////////////////////////////////////////////////


def get_correct_index(list_order, code):    # list_order = ["q", "w", "e", "r"]
    index_number = list_order.index(code)
    return index_number

# def dictionary_inverse(dict):
#     for key, value in dict.items():
#         rooms_title_inverse[value] = key
#     return rooms_title_inverse

def get_code_for_rm(lvl_info, room_type):
    this_rm = room_type.capitalize() + " Room"  # Red Room
    for i in range(len(lvl_info)):
        if lvl_info[i][title] == this_rm:
            return i


# ///////////   AFTER SELECTING CHOICE  //////////////////////////////////////
def if_active_skill(action1, lvl_info, player1, world1):
    action = lvl_info[LIST_ORDER.index(action1)][title]  # Bloodlust
    this_type = lvl_info[LIST_ORDER.index(action1)][skilltype]  # Active
    if this_type == "Active":
        print "\nYou used", action
        use_active_skill(action, player1)
        player1.calculate_total_power()
    # return player1

def use_active_skill(active_title, player1):
    if active_title == "Bloodlust":
        storez.bloodlust(player1)
    elif active_title == "Forced Cycle":
        storez.forced_cycle(player1)

# ///////////////////////////////

def find_response(action1, lvl_info, player):
    # action = choice_display[action1][title]
    # this_type = choice_display[action1][skilltype]
    action = lvl_info[LIST_ORDER.index(action1)][title]  # bloodlust
    this_type = lvl_info[LIST_ORDER.index(action1)][skilltype]  # Active
    if this_type == "Monster":
        print "\nYou enter the ", action
        next_level = go_to_next_room(action)
    elif this_type == "Active":
        next_level = "start_printing"
    else:
        print "You used", action
        next_level = "new_level"
    return next_level

def go_to_next_room(title):
    if title == "Red Room":
        return 'red_room'
    elif title == "Blue Room":
        return 'blue_room'
    elif title == "Yellow Room":
        return 'yellow_room'


# /////////////////////////////////////////////////////////////////////////////

def pik():
    print "This is my fight text, make it alright text"

# //////////////////////////////////////////////////////////////////////
# def initialize():
#     global EVERYTHING_LIBRARY
#     # f_display.print_card_stats(player1, "nodraw", world1)        # print "\n"
#
#     # intitialize
#     all_room_option_list = {}
#     all_room_option_list.update(room_list)
#     all_room_option_list.update(option_list)
#     all_skills = {}
#     all_skills.update(a_skills)
#     all_skills.update(p_skills)
#     all_skills.update(s_instants)
#
#
#     EVERYTHING_LIBRARY = {}
#     EVERYTHING_LIBRARY.update(all_skills)
#     EVERYTHING_LIBRARY.update(all_room_option_list)
#     return EVERYTHING_LIBRARY
