#!/usr/bin/python

# This is a game I made where you make your way through a number of dungeons
# and fight the last boss. Your power is determined by the 5 cards you draw
# for each dungeon. It is calculated as the sum of the cards you drawself.
# If your power is greater than the monster, you win, and you claim a prize.
# At the start of each level, you may choose which room to enter and you
# may see the power levels of the monster youy will face. You may also choose
# to "Skip" which will move you to the next level without fighting. You lose
# if you run out of health.

from sys import exit
from random import randint
from ex45_raw import *
import toolz
import f_display
# To keep dictionaries in the order they were made
# from collections import OrderedDict
import math
import os
from settings import *
from key_words import *
from other_area import *
import storez
import battle



class Choice(Scene):  # This is the main room where decisions will be made

    def enter(self):
        # os.system('cls')  # on windows
        # os.system('clear') # on linux
        # This one works -  self.test2()
        global player, world, skills_owned
        global rooms_att, options_att
        global choice_display

        # ------------------ DEATH CHECK
        if player[health] <= 0:
            return 'death'

        # ------------------ ROOM CHECK
        # Limits number of rooms and alerts when at final room
        world[current_level] += 1
        if world[current_level] > world[max_level]:
            print "\n"
            return 'finished'
        elif world[current_level] == world[max_level]:
            world[final_note] = "(FINAL ROOM)"

        # ------------------ STORE CHECK
        world[store_open] = toolz.check_store_open(world)
        if world[store_open] == "open":
            return 'store'

        # ------------------ HAND CHECK
        player[status] = toolz.check_hand_min_size(player)
        if player[status] == "dead":
            return 'pre-death'

        # ------------------SETUP - DRAW 5 NEW CARDS
        toolz.starting_phase(player, world)

        # ------------------MAKE ROOMS
        choice_display = f_display.rooms_make(room_list, option_list, skills_owned)
        choice_display = f_display.calc_monster_attack(world[current_level], choice_display)

        return 'choice2'


class Choice2(Scene):  # This is the main room where decisions will be made

    def enter(self):
        global player, world
        # ------------------PRINT - TITLE OF CURRENT ROOM
        f_display.print_level_bar(player, world)

        # ------------------PRINT - CARD STATS
        player = toolz.set_total_power(player, skills_owned)
        toolz.print_card_stats(player, "", world)

        #  ----------------PRINT ROOM DESCRIPTION
        toggle = 1  # toggle = 1 means show room descrip
        if world[current_level] % 5 != 1:
            toggle = 0
        toolz.print_room_description(toggle)  # you see before you 3 rms

        #  ------------------PRINT ROOM SELECTION
        f_display.print_rooms(choice_display)

        action1 = ""
        # This is in case input is not in dictionary
        # while action1 not in rooms_title:
        while action1 not in choice_display:
            action1 = raw_input("Select a room(q,w,e,r): ").lower()

            # ----- DIAGNOSTIC - type "show choice_display"
            if action1.lower()[:4] == "show":
                try:
                    vars()[action1.lower()[5:]]
                    print "try here"
                except KeyError:
                    print "no variable", action1.lower()[5:]
                else:
                    print vars()[action1.lower()[5:]]

        # Resolve all active skills first
        player = toolz.if_active_skill(action1, choice_display, player)

        # Finally move on to the next level
        next_level = toolz.find_response(action1, choice_display, player)
        return next_level



class Storefront(Scene):  # This is the store

    def enter(self):
        global player, world, skills_owned, skills_forsale

        # ------------------SETUP - TITLE OF CURRENT ROOM
        f_display.print_level_bar(player, world)

        # ------------------Display current deck and discard
        toolz.starting_phase(player, world)
        toolz.set_total_power(player, skills_owned)
        toolz.print_card_stats(player, "nodraw", world)

        # ------------------MAKE ROOMS
        skill_forsale = f_display.skill_forsale_make(a_skills, p_skills, s_instants)

        # ------------------FILLER GAP
        max_desc_rows = f_display.get_max_desc_rows(skill_forsale)
        print "\n"*(6 - int(max_desc_rows))

        # ------------DISPLAY skill_forsale
        f_display.print_skills_forsale(skill_forsale)

        # ------------get input
        action1 = ""
        while action1 not in skill_forsale:
            action1 = raw_input("Select a room(q,w,e,r): ").lower()


        new_buy = skill_forsale[action1][title].lower().replace(" ", "_")
        if skill_forsale[action1][skilltype] == "Instant":
            # player["health"] = player_health
            storez.get_store_instant(new_buy, s_instants, player)
            # player_health = player["health"]

        else:
            # You can have only one Active, one Passive, at any time
            # if a skill of the same type is bought (Active, Passive)
            # the old skill is overwritten
            for key, value in skills_owned.items():
                if value[skilltype] == all_skills[new_buy][skilltype]:
                    del skills_owned[key]
            skills_owned[new_buy] = all_skills[new_buy]

        return 'choice'

class StartMenu(object):
    # This is the first screen screen, and will teach player to use the "show"
    # and "hide" for menu items (health, hand, deck, descriptions, etc) so that
    # they will know how to hide them later on
    def enter(self):
        # global deck, hand, discard, power
        toolz.print_card_stats(player, "nodraw", world)
        # print "\n"
        return 'choice'

        print "Welcome to the cave"
        print "This is the tutorial"
        action1 = raw_input("Type 'Show Menu' to begin >")
        # action1 = raw_input("Type 'Show Menu' (%d Steps left)>" %step count)

        # start_menu.print_part_1(player_health, health_show, hand, hand_show)
        # start_menu.print_part_2(deck, deck_show, discard, discard_show)

        # print_health(player_health, health_show)
        # print_hand(hand, hand_show)
        # print_deck(deck, deck_show)
        # print_discard(discard, discard_show)
        # print_room_desc(room_desc, room_desc_show)
        time.sleep(60)
        return 'choice'

class RedRoom(Scene):
    def enter(self):
        global choice_display

        # Get the monster attack for this room
        this_rm = "Red Room"
        this_rm_code = toolz.get_code_for_rm(choice_display, this_rm)
        if this_rm_code == "":
            print "no code found for ", this_rm, "\nin here", choice_display
        monster_attack = choice_display[this_rm_code][desc]
        player_attack = player[power]

        # ------------------FIGHT TEXT
        battle.show_fight_text(monster_attack, player_attack)

        # ------------------RESOLUTION
        fight_result = battle.fight_resolution(player_attack, monster_attack)
        if fight_result == "win":
            reward_text = battle.red_prize(world[current_level], player[discard])
            print "\n", arrow,"Win!" + reward_text
        elif fight_result == "half_win":
            reward_text = battle.red_prize(world[current_level], player[discard])
            player[health] = toolz.take_damage(player[health], 1)
            damage_text = toolz.text_take_damage(player[health], 1)
            print "\n", arrow,"Half-Win!" + reward_text + ", received damage (-1) hp"
        else:
            player[health] = battle.lose_fight(player[health])
            print "\n", arrow,"Defeated! received damage (-1) hp"

        return 'choice'

class BlueRoom(Scene):

    def enter(self):
        global choice_display

        # Get the monster attack for this room
        this_rm = "Blue Room"
        this_rm_code = toolz.get_code_for_rm(choice_display, this_rm)
        if this_rm_code == "":
            print "no code found for ", this_rm, "\nin here", choice_display
        monster_attack = choice_display[this_rm_code][desc]
        player_attack = player[power]

        # ------------------FIGHT TEXT
        battle.show_fight_text(monster_attack, player_attack)

        # ------------------RESOLUTION
        fight_result = battle.fight_resolution(player_attack, monster_attack)
        if fight_result == "win":
            reward_text = battle.blue_prize(player[hand], player[discard])
            print "\n", arrow,"Win!" + reward_text
        elif fight_result == "half_win":
            reward_text = battle.blue_prize(player[hand], player[discard])
            player[health] = toolz.take_damage(player[health], 1)
            toolz.text_take_damage(player[health], 1)
            print "\n", arrow,"Half-Win!" + reward_text + ", received damage (-1) hp"
        else:
            player[health] = battle.lose_fight(player[health])
            print "\n", arrow,"Defeated! received damage (-1) hp"

        return 'choice'

class YellowRoom(Scene):
    def enter(self):
        global choice_display

        # Get the monster attack for this room
        this_rm = "Yellow Room"
        this_rm_code = toolz.get_code_for_rm(choice_display, this_rm)
        if this_rm_code == "":
            print "no code found for ", this_rm, "\nin here", choice_display
        monster_attack = choice_display[this_rm_code][desc]
        player_attack = player[power]

        # ------------------FIGHT TEXT
        battle.show_fight_text(monster_attack, player_attack)

        # ------------------RESOLUTION
        fight_result = battle.fight_resolution(player_attack, monster_attack)
        if fight_result == "win":
            reward_text = battle.yellow_prize(world[current_level], player[discard])
            print "\n", arrow,"Win!" + reward_text
        elif fight_result == "half_win":
            reward_text = battle.yellow_prize(world[current_level], player[discard])
            player[health] = toolz.take_damage(player[health], 1)
            toolz.text_take_damage(player[health], 1)
            print "\n", arrow,"Half-Win!" + reward_text + ", received damage (-1) hp"
        else:
            player[health] = battle.lose_fight(player[health])
            print "\n", arrow,"Defeated! received damage (-1) hp"
        return 'choice'



class EndBriefing(Scene):
    def enter(self):
        global player_health, current_level
        toolz.dump_all(player[hand], player[discard])
        toolz.dump_all(player[discard], player[deck])
        print "Highest Level Reached: ", player[current_level]
        start_menu.print_health(player[health], "1")
        print "deck:    ", str(len(player[deck]))+"x", "cards", player[deck]
        return 'death'


class Map(object):

    scenes = {
        'red_room': RedRoom(),
        'blue_room': BlueRoom(),
        'yellow_room': YellowRoom(),
        'choice': Choice(),
        'choice2': Choice2(),
        'start_menu': StartMenu(),
        'pre-death': EndBriefing(),
        'store': Storefront(),
        # Used in original sample file
        # 'central_corridor': CentralCorridor(),
        # 'laser_weapon_armory': LaserWeaponArmory(),
        # 'the_bridge': TheBridge(),
        # 'escape_pod': EscapePod(),
        'death': Death(),
        'finished': Finished(),
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)

a_map = Map('start_menu')
# a_map = Map('choice')
# a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()
