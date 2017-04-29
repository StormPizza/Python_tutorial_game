from sys import exit
from random import randint
import enemies
import math
import time
from settings import *
import storez
import store_instants


def transfer_random(fromlist, destlist, times):
    # transfers random cards from the FROMLIST to the DESTLIST
    # TIMES is the number of cards moved
    count = 0
    if times < 1:  # If TIMES is less than one, exit function
        return

    while count < times:
        index = randint(0, len(fromlist)-1)
        destlist.append(fromlist[index])
        fromlist.remove(fromlist[index])
        count += 1

def print_room_description(toggle):
    # if current_level % 5 != 1:
    if toggle == 0:
        print "\n \n \n \n \n"
        return
    print "\n", spaces5, "You see before you three rooms:"
    print spaces5, "  The Red rewards you with a POWERFUL new card, "
    print spaces5, "  The Blue burns the LOWEST card that has been used"
    print spaces5, "  The Yellow rewards you with three WEAK new cards \n"


def starting_phase(player, world):
    # print_card_stats(deck, hand, discard, draw)
    # time.sleep(0.5)
    # print "\ndeck:    ", len(deck), " cards"  # deck
    player[current_effects] = {}
    for key, value in skills_owned.items():
        if value[skilltype] == "Passive" and value[trigger] != from_hand:
            player[current_effects] = add_current_effect(player, key)

    dump_hand(player)
    # Draw up to 5 cards into hand from deck
    # If deck has less than 5 card, draw all cards and add discard into deck
    # DRAW PHASE - Draw cards until you have 5
    if world[store_open] != "open":
        player = draw_full_hand(player)

def print_card_stats(player, draw, world):
    # print player[current_effects]
    print "deck:     ", str(len(player[deck]))+"x", "cards", player[deck]
    # time.sleep(0.5)
    bump = " " * (2-len(str(len(player[discard]))))
    print "discard:", bump, str(len(player[discard]))+"x", "cards", player[discard]

    # Row #4 - Hand
    if draw != "nodraw":
        hand_print1 = "            You draw up to 5 cards -->> "
    else:
        hand_print1 = "                                        "
    hand_print2 = "hand: "+ str(len(player[hand]))+"x "+ "cards " + str(player[hand])

    print hand_print1, hand_print2
    # print player

    # Row #5 - Bonus Power
    if len(player[current_effects]) != 0:
        bonus_print1 = ""
        # print player[current_effects]
        for key, value in player[current_effects].items():
            times2 = ""
            # print value, player[current_effects], "LOOK HERE"
            if value > 1:
                times2 = " x" + str(value)

            bonus_print1_add = all_skills[key][title] + times2
            if bonus_print1 != "":
                if all_skills[key][skilltype] == "Active":
                    bonus_print1 = bonus_print1_add + ", " + bonus_print1
                elif all_skills[key][skilltype] == "Passive":
                    bonus_print1 = bonus_print1 + ", " + bonus_print1_add
            else:
                bonus_print1 = bonus_print1_add

        bonus_print = "(" + bonus_print1 + "!) "+ "<+" + str(player[bonus_power]) + ">"

    else:
        bonus_print = ""
    b_indent_count = len(hand_print1)+len(hand_print2)-len(bonus_print)
    print b_indent_count*" ",
    print bonus_print

    # Row #6 - Total Power - cumulated
    if world[store_open] == "open" or world[current_level] == 0:
        hand_print3 = ""
    else:
        hand_print3 = "Your Total Power >>>>    " + str(player[power]) + "     <<<<<<"
    print hand_print3

# //////////////////////////////////////////////////////////////////////////////


def set_temp_bonus_power(player, skills_owned):
    player[temp_bonus_power] = 0
    # print player[current_effects]

    for key, value in player[current_effects].items():
        effects_no = player[current_effects][key]
        if all_skills[key][skilltype] != "Passive":  # Passives are not temp

            player[temp_bonus_power] += all_skills[key][ef_value][1] * effects_no
        elif key == "double_power":
            player[temp_bonus_power] += all_skills[key][ef_value][1] * effects_no
            # if key = "bloodlust":

                # player[current_effects] = add_current_effect(player, "bloodlust")

        # if skills_owned[key][skilltype] == "Passive":
    return player[temp_bonus_power]

def set_perm_bonus_power(player, skills_owned): # Resets stats down to minimum
    # print player, "set perm_bonus_power"
    # bonus_total = 0
    player[perm_bonus_power] = 0  # If no passive effects are found
    # player[current_effects] = {}
    for key, value in skills_owned.items():
        if value[skilltype] == "Passive":
            player[perm_bonus_power] = storez.get_passive_power(skills_owned, player, world)
            # player[current_effects] = add_current_effect(player, key)


    return player[perm_bonus_power]

def set_bonus_power(player):
    player[bonus_power] = 0
    player[bonus_power] += set_perm_bonus_power(player, skills_owned)
    player[bonus_power] += set_temp_bonus_power(player, skills_owned)
    return player[bonus_power]

def get_card_power(player):  # Calc total power from 5 cards in hand
    # print player
    player[card_power] = 0
    # power = player[perm_power]  # baseline power
    # print player
    # ----- Add Power from sum of cards drawn
    for i in player[hand]:
        player[card_power] += int(i)
    return player[card_power]

def set_total_power(player, skills_owned):
    player[power] = 0
    player[power] += get_card_power(player)
    player[power] += set_bonus_power(player)
    return player

# player[current_effects] = {}
# player[current_effects] =

def add_current_effect(player, skill_name):
    # for key, value in player[current_effects].items():
    # print type(player[current_effects])
    # print type(player[discard])
    if skill_name in player[current_effects]:
        player[current_effects][skill_name] += 1
    else:
        player[current_effects][skill_name] = 1
    return player[current_effects]


def add_space(code, maxlen, press):
    # Makes the string length equal to the length of maxlen, and then centered
    # Both code and maxlen are strings, code = "q", maxlen = "Yellow Room"
    if len(code) < len(maxlen):
        bump = (len(maxlen) - len(code) - len(press)) % 2
        sp = (len(maxlen) - len(code) - len(press))/2
        code = " "*(sp+bump) + press + code + " "*(sp)
        # print code
    return code

    # newset1.append(set1)
def get_correct_index(list_order, code):
    # list_order = ["q", "w", "e", "r"]
    index_number = list_order.index(code)
    return index_number

def take_damage(player_health, damage):
    player_health -= damage
    # text_take_damage(player_health, damage)
    return player_health

def text_take_damage(player_health, damage):
    print arrow, "Unfortunately you take %d damage" % damage
    print arrow, "Player_health: %d ---" % player_health, "H " * player_health

def draw_full_hand(player):
    # draw up to 5 cards
    if len(player[deck]) < 5:
        transfer_random(player[deck], player[hand], len(player[deck]))
        transfer_random(player[discard], player[deck], len(player[discard]))

    transfer_random(player[deck], player[hand], 5-len(player[hand]))

    # Check for auto-trigger skills
    for key, value in skills_owned.items():  # Passive, but auto-trigger
        if key == "double_power":
            # player[current_effects]["double_power"] = 1
            # player[temp_bonus_power] += set_temp_bonus_power_from_hand(player, "double_power")
            player[current_effects] = set_effects_from_draw(player, "double_power")
    # return player

def set_effects_from_draw(player, passive_name): # double_power
    # print player[current_effects], "set effects from draw"
    for key, value in player[current_effects].items():
        if all_skills[key][trigger] == "from_hand":
            del player[current_effects][key]
    # hand_bonus = 0  # this can be zeroed
    count_list = {}  # count how many of each card there are in hand
    # Check for double_power
    for i in player[hand]:
        if i in count_list:
            count_list[i] += 1
        else:
            count_list[i] = 1
    # print count_list
    # Apply double_power - only if applicable
    for key, value in count_list.items():
        if count_list[key] > 1 and key > 0:
            # print all_skills[passive_name][ef_value][1]
            # hand_bonus += all_skills[passive_name][ef_value][1]
            add_current_effect(player, passive_name)
    # return hand_bonus
    # print player[current_effects], "set after effects from draw"
    return player[current_effects]

def dump_hand(player):
    transfer_random(player[hand], player[discard], len(player[hand]))
    # discard.append(7)

def dump_all(fromlist, tolist):
    transfer_random(fromlist, tolist, len(fromlist))

def dictionary_inverse(dict):
    for key, value in dict.items():
        rooms_title_inverse[value] = key
    return rooms_title_inverse

def get_code_for_rm(choice_display, this_rm):
    found_code = ""
    for key, value in choice_display.items():
        if value[title] == this_rm:
            found_code = key
    return found_code


def check_hand_min_size(player):
    total_cards = len(player[hand])+len(player[deck])+len(player[discard])
    if total_cards < 5:
        print "You do not have enough cards to make a full hand."
        print "You die from incomplete-hand syndrome"
        return 'dead'

def check_store_open(world):
    store_status = "closed"
    # print world
    # print world[current_level]
    if world[current_level] < 1:
        return store_status
    if world[current_level] % world[store_interval] == 0:
        store_status = "open"
    return store_status


# ///////////   AFTER SELECTING CHOICE  //////////////////////////////////////
def if_active_skill(action1, choice_display, player):
    action = choice_display[action1][title]
    this_type = choice_display[action1][skilltype]
    if this_type == "Active":
        print "\nYou used ", action
        player = use_active_skill(choice_display[action1][title], player)
        # print player[power], "if active skill"
        # next_level = "choice2"
    return player

def use_active_skill(active_title, player):
    if active_title == "Bloodlust":
        player = storez.bloodlust(player)
    elif active_title == "Forced Cycle":
        player = storez.forced_cycle(player)
    # print player[health], "use active skill"
    return player

# ///////////////////////////////

def find_response(action1, choice_display, player):
    action = choice_display[action1][title]
    this_type = choice_display[action1][skilltype]
    if this_type == "Monster":
        print "\nYou enter the ", action
        next_level = go_to_next_room(choice_display[action1][title])
    elif this_type == "Active":
        next_level = "choice2"
    else:
        print "You used ", action
        next_level = "choice"
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
