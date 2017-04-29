from sys import exit
from random import randint
import enemies
import math
import time
import copy
import toolz
from settings import *
# from __future__ import print_function

# //////////////////////////////////////////////////////////////////////////
# //  TOP OVERLAY FOR EACH FLOOR   ///////////////////////////////////////////
def print_level_bar(player1, world1):
    level_text = "LEVEL " + str(world1.current_level)  # LEVEL 5
    if world1.level_type == "we_at_store":
        level_text = "STORE // " + level_text
    # title1_dashes_length = SCREEN_LENGTH - len(health2) - len(margin)
    title = margin + level_text + margin + world1.final_note + DASHES
    print title
    #    LEVEL 1   ///////////////////////////////////////////////////////
    #   STORE // LEVEL 5   ///////////////////////////////////////////////////////
    # print player1.health
    health_icons = "H " * player1.health
    health_value = "    Player health: (" + str(player1.health) + " hp) "
    health2 = health_value + health_icons
    title2_dashes_length = SCREEN_LENGTH - len(health2) - len(margin)
    title2_dashes1 = title2_dashes_length * "/"
    title2 = title2_dashes1 + health2 + margin

    print title2, "\n"

# //////////////////////////////////////////////////////////////////////////
# //  MIDDLE OVERLAY FOR EACH FLOOR   ///////////////////////////////////////////
def print_card_stats(player1, draw, world1):  # 5 Rows

    # FINAL OUTPUT ( without numbers on left)
    #1     deck:      5x cards [1, 1, 1, 1, 1]
    #2 discard:   0x cards []
    #3             You draw up to 5 cards -->>  hand: 5x cards [1, 1, 0, 0, 0]
    #4                                                      (Bloodlust!) <+10>
    #5 Your Total Power >>>>    13     <<<<<<

    # ROW #1     //////////////////////////////////////////////////////////////
    # row1 = "deck:     ", str(len(player1.deck))+"x", "cards", player1.deck
    print "deck:     ", str(len(player1.deck))+"x", "cards", player1.deck
    # time.sleep(0.5)

    # ROW #2  //////////////////////////////////////////////////////////////
    bump = " " * (2-len(str(len(player1.discard)))) # num of digits of discard count
    # row2 = "discard:", bump, str(len(player1.discard))+"x", "cards", player1.discard
    print "discard:", bump, str(len(player1.discard))+"x", "cards", player1.discard

    # Row #3 - Hand   ///////////////////////////////////////////////////////
    if world1.level_type == "we_be_fighting":  # hand_print1 = "  You draw up to 5 cards -->> "
        hand_print1 = ("You draw up to 5 cards -->> ").rjust(40, " ")
    else:
        hand_print1 = 50 * " "
    hand_print2 = "hand: "+ str(len(player1.hand))+"x cards " + str(player1.hand)
    row3 = hand_print1 + hand_print2
    print row3

    # Row #4 - Bonus Power (Bloodlust, Sharpened, Half-Sharp) ////////////////
    bonus_print1 = ""        # print player1.current_effects]
    bonus_print = ""
    if player1.current_effects and world1.level_type == "we_be_fighting":
        # if current_effects is not empty
        for key, value in player1.current_effects.items():  # x2
            times2 = ""
            if value > 1:
                times2 = " x" + str(value)

            bonus_print1_add = all_skills[key][title] + times2  #  Bloodlust x2
            if bonus_print1:
                if all_skills[key][skilltype] == "Active":
                    bonus_print1 = bonus_print1_add + ", " + bonus_print1
                elif all_skills[key][skilltype] == "Passive":
                    bonus_print1 = bonus_print1 + ", " + bonus_print1_add
            else:
                bonus_print1 = bonus_print1_add

        bonus_print = "(" + bonus_print1 + "!) "+ "<+" + str(player1.bonus_power) + ">"

    b_indent_count = SCREEN_LENGTH - len(bonus_print)
    row4 = b_indent_count*" " +  bonus_print
    print row4

    # Row #5 - Total Power - cumulated  ///////////////////////////////////////
    row5 = ""
    if world1.level_type != "we_at_store" and world1.current_level != 0:
        row5 = "Your Total Power >>>>    " + str(player1.power) + "     <<<<<<"
    print row5

def print_room_description(world1, options):
    # print "//////////////////////"

    # if current_level % 5 != 1:
    # toggle = 1  # toggle = 1 means show room descrip
    rd_set = []
    max_desc_rows = len(options[0])
    for i in range(12 - int(max_desc_rows)):
        rd_set.append("")

    # print "\n"*(11 - int(max_desc_rows))
    # return
    # if world1.level_type == "we_at_store":  # Store
    #     max_desc_rows = len(options[0])
    #     print "\n"*(11 - int(max_desc_rows))
    #     return
    if world1.current_level % world1.room_desc_interval == 1 and world1.level_type == "we_be_fighting":  # Fight
        # print "\n" * 5
        # return
        # print "\n", spaces5, "You see before you three rooms():"
        rd_set[1]=spaces5+"Monsters with a lower power lose immediately, others may not: "
        rd_set[2] = spaces5+"  The Red Room rewards you with a POWERFUL new card, "
        rd_set[3] = spaces5+"  The Blue Room burns the LOWEST card that has been used"
        rd_set[4] = spaces5+"  The Yellow Room rewards you with three WEAK new cards"
    # print "\n"
    for line in rd_set:
        print line
    # print len(rd_set)
    # print "//////////////////////"
    return

# /////////////////////////////////////////////////////////////////////////////

def copy_rand_items(from_list, to_list, num_to_move):
    # this only adds items to the very end of the list

    # dict item has pre-defined order number, add to list first, then sort later
    # if dict item has MUST-ADD, then add to list first
    temp_to_list = []
    temp_from_list = copy.copy(from_list)
    # PART 1 - first add the must adds
    for key in temp_from_list:
        if EVERYTHING_LIBRARY[key][option_freq] == "ALWAYS":
            temp_to_list.append(EVERYTHING_LIBRARY[key])
            temp_from_list.remove(key)

    # PART 2 - Add the Remaining Ones
    # will only grab up to the number of items needed
    # or while there is a list to grab from
    while len(temp_to_list) < num_to_move and len(temp_from_list) > 0:
        # Randomly select an item from list
        rand_index = randint(0, len(temp_from_list)-1)
        key = temp_from_list[rand_index]
        temp_to_list.append(EVERYTHING_LIBRARY[key])
        temp_from_list.remove(key)

    # PART 3 - Sort - this gets complicated
    get_order = lambda key: key[option_order]
    # get_order = lambda key: key

    order_list = map(get_order, temp_to_list)  # a list like ["",3,1,2]
    order_and_tempto = zip(order_list, temp_to_list)  # linking the list to order
    order_and_tempto.sort()  # this is where sorting happens
    temp_to_list = [tempto for order, tempto in order_and_tempto]  # stuff
    # [x for (y,x) in sorted(zip(Y,X))] See this

    # PART 4 - return to list
    for item in temp_to_list:
        to_list.append(item)

    # to_list is a list of dictionaries
    return to_list

def Create_Display_Info(player1, world1):
    lvl_info = []    # Make dict of 5  - 1,2,3 are rooms

    if world1.level_type == "we_be_fighting":
        # add 3 rooms to lvl_info, and gives them order code "q, w, e"
        lvl_info = copy_rand_items(room_list, lvl_info, ROOMS_NO)
        # add 1 skip  to lvl_info, and gives them order code "r"
        lvl_info = copy_rand_items(other_list, lvl_info, OPTIONS_NO)
        # add 1 skill to lvl_info, and gives them order code "a"
        equipped_actives = []
        for key, value in player1.skills_owned.items():
            if player1.skills_owned[key][skilltype] == "Active":
                equipped_actives.append(key)
        lvl_info = copy_rand_items(equipped_actives, lvl_info, len(equipped_actives))

    elif world1.level_type == "we_at_store":
        # adds 2 active skills to lvl_info, and assigns order code "q, w"
        active_list2 = exclude_owned_skills(player1, active_list)
        lvl_info = copy_rand_items(active_list2, lvl_info, active_no)
        # adds 2 passive skills to lvl_info, and assigns order code "e, r"
        passive_list2 = exclude_owned_skills(player1, passive_list)
        lvl_info = copy_rand_items(passive_list2, lvl_info, passive_no)
        # adds 1 instant skills to lvl_info, and assigns order code "a"
        lvl_info = copy_rand_items(instant_list, lvl_info, instant_no)
    else:
        exit(1)

    for i in range(len(lvl_info)):
        lvl_info[i][code] = LIST_ORDER[i]
    # to_list is a list of dictionaries

    # lvl_info =
    # code: q             code: w             code: e             code: r
    # option_order: 1     option_order: 2     option_order: 3     option_order: 4
    # trigger:            trigger:            trigger:            trigger:
    # effect_target:      effect_target:      effect_target:      effect_target:
    # title: Red Room     title: Blue Room    title: Yellow Room  title: Skip
    # ef_value: [0, 0]    ef_value: [0, 0]    ef_value: [0, 0]    ef_value: [0, 0]
    # type: Monster       type: Monster       type: Monster       type:
    # option_freq: ALWAYS option_freq: ALWAYS option_freq: ALWAYS option_freq: ALWAYS
    # desc:               desc:               desc:               desc:
    return lvl_info

    # for key, value in lvl_info[0].items():
    #     for i in range(len(lvl_info)):
    #         text3 = key + ": " + str(lvl_info[i][key])
    #         text2 = text3.ljust(19, " ")
    #         print text2,
    #     print " "
    # raw_input(" ")

def Format_Display_Info(lvl_info, world1, new_word1):
    # Formats them into squares but without the border
    # This gets the length of the longest list in the list
    max_desc_rows = len(max(new_word1, key=len))
    options = []
    # print len(lvl_info), len(new_word1)
    for i in range(len(lvl_info)):  # there are 5 options in all
        options.append([])

        options[i].append(lvl_info[i][title].center(TEXTLEN, " "))  # Red Room

        if world1.level_type == "we_be_fighting":
            if lvl_info[i][skilltype]:
                skilltype_2 = "("+lvl_info[i][skilltype]+")"
            else:
                skilltype_2 = ""

            monsterpower_2 = lvl_info[i][ef_value][0]
            monsterpower_2 = "Power: " + str(monsterpower_2)
            if lvl_info[i][skilltype] != "Monster":
                monsterpower_2 = ""

            options[i].append(skilltype_2.center(TEXTLEN, " "))  # (Monster)
            options[i].append(monsterpower_2.center(TEXTLEN, " "))  # Power: 7

        elif world1.level_type == "we_at_store":
            skilltype_2 = "(" + lvl_info[i][skilltype] + ")"
            options[i].append(skilltype_2.center(TEXTLEN, " "))  # (Active)
            options[i].append(" ".center(TEXTLEN, " "))  # --Space--
            for desc_line in new_word1[i]:
                options[i].append(desc_line.center(TEXTLEN, " "))  # Return All

            extra_spaces = max_desc_rows - len(new_word1[i])
            # for times in extra_spaces:
            for times in range(extra_spaces):
                options[i].append(" ".center(TEXTLEN, " "))

        options[i].append(" ".center(TEXTLEN, " "))  # -- Space--

        code_input = "Press: " + LIST_ORDER[i]
        options[i].append(code_input.center(TEXTLEN, " "))

    # options =
    #    Red Room            Red Room            Red Room            Red Room
    #   (Monster)           (Monster)           (Monster)           (Monster)
    #   Power: -1           Power: -1           Power: -1           Power: -1
    #
    #    Press: q            Press: q            Press: q            Press: q

    # options = [[title], [skilltype], [desc]],     [[title], [skilltype], [desc]]
    return options # in a printable format, just without borders


def Print_Display(options):
    # print options[0]
    print ((" " + ("="*TEXTLEN)) * len(options)) + " "
    for j in range(len(options[0])):
        print_text = ""
        for i in range(len(options)):
            # print "|".join([str(x) for x in options[i][j]]) + "|"
            print_text += "|" + options[i][j]
            # print "|" + options[i][j],
        print print_text + "|"
    print ((" " + ("="*TEXTLEN)) * len(options)) + " "
    return


# /////////////////////////////////////////////////////////////////////////////
# ////   FIGHT LEVEL DISPLAY   ////////////////////////////////////////////////
# #  ============== ============== ============== ============== ==============
# # 1| Yellow Room  | Red Room     | Red Room     |     Skip     |  Force Cycle |
# # 2|  Monster     |  Monster     |  Monster     |  (Ability)   |  (Ability)   |
# # 3|     Power: 1 |     Power: 1 |     Power: 1 |              |              |
# # 4|              |              |              |              |              |
# # 5|   enter: Q   |   enter: Q   |   enter: Q   |   enter: Q   |   enter: Q   |
# #  ============== ============== ============== ============== ==============
#
# /////////////////////////////////////////////////////////////////////////////


# /////////////////////////////////////////////////////////////////////////////
# //////////   STORE   DISPLAY  ///////////////////////////////////////////////
# /////////////////////////////////////////////////////////////////////////////
#
#     #      ============== ============== ============== ==============
#     #    | Forced Cycle | Double Power |  Half Sharp  |    Medic     |
#     #    |   (Active)   |  (Passive)   |  (Passive)   |  (Instant)   |
#     #    |              |              |              |              |
#     # 1  | Return all   | Pairs in hand| Permanently  | Gain (2) hp  |
#     # 2  |cards to the  | give <+5>    |gain <+2>     | immediately  |
#     # 3  |     deck     |    power     |    power     |              |
#     #    |              |              |              |              |
#     #    |   enter: q   |   enter: w   |   enter: e   |   enter: r   |
#     #     ============== ============== ============== ==============
#
#//////////////////////////////////////////////////////////////////////////

def calc_monster_attack(world1, lvl_info):
    if world1.level_type == "we_at_store":
        return lvl_info
    power = {}  # ------------------ASSIGN MONSTER VALUE
    power['Red Room']    = randint(-2, 4) + world1.current_level
    power['Blue Room']   = randint(-2, 4) + world1.current_level/2
    power['Yellow Room'] = randint( 2, 4) + world1.current_level

    for code in lvl_info:
        # print len(lvl_info)
        if code[skilltype] == "Monster":
            code[ef_value][0] = power[code[title]]
    return lvl_info

def exclude_owned_skills(player1, skill_set):
    # This makes sure the store does not show skills that are already owned
    # for item in skill_set:
    #     if item in player1.skills_owned:
    #         skill_set.remove(item)
    skill_set2 = filter(lambda x: x not in player1.skills_owned, skill_set)
    return skill_set2

def make_desc_list(lvl_info):
    # 1  | Return all   | Pairs in hand| Permanently  | Gain (2) hp  |
    # 2  |cards to the  | give <+5>    |gain <+2>     | immediately  |
    # 3  |     deck     |    power     |    power     |              |
    # max_desc_rows = 1
    # new_word1 = [[]] * (len(lvl_info))
    # print "//////////////////////// START"
    new_word1 = []
    # MARGIN2 = 2
    for i in range(len(lvl_info)):
        new_word1.append([])
    for i in range(len(lvl_info)):  # sometimes less than 5
        # print len(lvl_info)
        text1 = lvl_info[i][desc]  # text1 = "Return all cards to the deck"
        word1 = text1.split()
        # print word1

        sum2 = ""
        for j in range(len(word1)):
            # if the next word to add will push it past 14 characters
            if len(sum2 + " " + word1[j]) > TEXTLEN:
                if sum2:
                    # print sum2
                    # print new_word1, "TEST1"
                    new_word1[i].append(sum2)
                    # print new_word1, "TEST2"
                    sum2 = word1[j]
                # hope to not use but just in case word is too long, we cut
                if len(word1[j]) > TEXTLEN:
                    new_word1[i].append(word1[j][:TEXTLEN])
                    sum2 = word1[j][TEXTLEN:]
            else:
                if not sum2:
                    sum2 = word1[j]
                else:
                    sum2 = sum2 + " " + word1[j]
        # print i, sum2, new_word1
            # print "//////////////////////////////////////////////////////////////////"
            # for k in range(len(new_word1)):
            #     print i, j, new_word1[k]
                # print lvl_info[i]

        # print new_word1
        new_word1[i].append(sum2)

        # print i

    # print "//////////////////////// END"

    return new_word1
