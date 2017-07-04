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
# from other_files.ex45_raw import *
from other_files import toolz
from other_files import room_create
from other_files import f_display
from other_files.settings import *
from other_files import storez
from other_files import battle
from other_files import player_class

# To keep dictionaries in the order they were made
# from collections import OrderedDict
import math
import os

# StartMenu - Level_Setup - Print_Screen_Part - Fight_Level-Battle - Victory - Death
#                         - Store_Level
# Each LEVEL might be a Fight_Level or a Store_Level
# In Fight_Levels, you choose between three rooms to fight
class Scene(object):

    def enter(self):
        print "This scene is not yet configured."
        print "Subclass it and implement enter()."
        exit(1)

# ////////////////////////////////////////////////////////////////////////////

class StartMenu(object):
    # This is the first screen screen, and will teach player to use the "show"
    # and "hide" for menu items (health, hand, deck, descriptions, etc) so that
    # they will know how to hide them later on EDIT - DONT GO THIS ANYMORE
    def enter(self):
        global player1        # global deck, hand, discard, power

        print arrow, "GAME STARTED"
        return 'new_level'
        # print "Welcome to the cave"
        # print "This is the tutorial"
        # # action1 = raw_input("Type 'Show Menu' to begin >")
        # time.sleep(60)
        # return 'fight'

class New_Level(Scene):  # This is the main room where decisions will be made

    def enter(self):
        global player1, world1
        # ------------------ GET NEW LEVEL TYPE ( FIGHT, STORE, WIN OR DEAD )
        # ------------------SETUP 1 - TITLE OF CURRENT LEVEL
        current_level_type = room_create.get_level_type(player1, world1)
        if current_level_type:  # also moves to the next room
            return current_level_type  # 'store', 'fight'


class Level_Setup(Scene):  # The information for the screen display is calculated here
    # Screen Display is made of four parts (- with information):
    # 1 Status Bar - Current level, HP
    # 2 Card Bar - Deck, Discard, Hand, Active Bonuses, and Totaled Power
    # 3 Room Description
    # 4 Options Bar - selection of up to 5 choices (5 max), Enter choice below
    def __init__(self, current_level_type):
        self.room_type = current_level_type  # FIGHT, STORE

    def enter(self):
        # os.system('cls')  # on windows
        # os.system('clear') # on linux     # This one works -  self.test2()
        global player1, world1
        global lvl_info, new_word1, options

        # ------------------SETUP 2 -  DRAW 5 NEW CARDS CARD STATS - AFTER DRAWING
        toolz.starting_phase(player1, world1)  # Draw5, clear Effects
        player1.calculate_total_power()

        #  ------------------SETUP 4 - CREATE OPTION SELECTION
        # Each LEVEL has 3 rooms, 1 general, and 1 active skill
        lvl_info = f_display.Create_Display_Info(player1, world1)
        lvl_info = f_display.calc_monster_attack(world1, lvl_info)
        new_word1 = f_display.make_desc_list(lvl_info)
        options = f_display.Format_Display_Info(lvl_info, world1, new_word1)

        return 'start_printing'


class Print_Screen_Part(Scene):  #

    def enter(self):
        global player1, world1, options
        # ------------------SETUP 1 - TITLE OF CURRENT LEVEL
        f_display.print_level_bar(player1, world1)
        # ------------------SETUP 2 - CARD STATS
        f_display.print_card_stats(player1, "", world1)
        #  -----------------SETUP 3 -PRINT FIGHT ROOM DESCRIPTION
        f_display.print_room_description(world1, options)  # you see before you 3 rms
        #  ------------------SETUP 4 -PRINT FIGHT ROOM SELECTION
        f_display.Print_Display(options)

        if world1.level_type == "we_at_store":
            return 'store_input'
        elif world1.level_type == "we_be_fighting":
            return 'fight_input'


class Get_Fight_Input(Scene):  # ------------GET INPUT

    def enter(self):

        action1 = ""
        get_order = lambda key: key[code]
        code_list = map(get_order, lvl_info)  # [q,w,e,r]

        while action1 not in code_list:  # In case input is not in dictionary
            action1 = raw_input("Select a room( q,w,e,r,a ): ").lower()

            # ----- DIAGNOSTIC - type "show lvl_info"
            if action1.lower()[:4] == "show":
                try: vars()[action1.lower()[5:]]
                except KeyError: print "no variable", action1.lower()[5:]

        # Resolve all active skills first
        toolz.if_active_skill(action1, lvl_info, player1, world1)

        # Finally move on to the next level
        next_level = toolz.find_response(action1, lvl_info, player1)
        return next_level

class Fight_Level_Battle(Scene):
    def __init__(self, color):
        self.room_type = color  # Red, Blue, or Yellow
    def enter(self):
        global lvl_info

        # Get the monster attack for this room
        this_rm_code = toolz.get_code_for_rm(lvl_info, self.room_type)
        monster_attack = lvl_info[this_rm_code][ef_value][0]
        player_attack = player1.power

        # ------------------FIGHT TEXT
        battle.show_fight_text(monster_attack, player_attack)

        # ------------------Fight Resolution
        fight_result = battle.fight_resolution(player_attack, monster_attack)
        print "\n", arrow,
        if fight_result == "win":
            reward_text = self.find_prize(self.room_type)
            print "Win!" + reward_text
        elif fight_result == "half_win":
            reward_text = self.find_prize(self.room_type)
            player1.take_damage(1)
            player1.text_take_damage(1)
            print "Half-Win!" + reward_text + ", received damage (-1) hp"
        else:
            battle.lose_fight(player1)
            print "Defeated! received damage (-1) hp"

        return 'new_level'

    def find_prize(self, color):
        if color == "red":
            reward_text = battle.red_prize(world1.current_level, player1.discard)
        elif color == "blue":
            reward_text = battle.blue_prize(player1.hand, player1.discard)
        elif color == "yellow":
            reward_text = battle.yellow_prize(world1.current_level, player1.discard)
        return reward_text




class Get_Store_Input(Scene):  # ------------GET INPUT

    def enter(self):
        action1 = ""
        get_order = lambda key: key[code]
        code_list = map(get_order, lvl_info)
        while action1 not in code_list:
            action1 = raw_input("Select a room(q,w,e,r,a): ").lower()
        new_buy = lvl_info[code_list.index(action1)][title].lower().replace(" ", "_")
        if lvl_info[code_list.index(action1)][skilltype] == "Instant":
            storez.get_store_instant(new_buy, s_instants, player1)
        else:
            # You can have only one Active and one Passive, at any time
            # if a skill of the same type is bought (Active, Passive)
            # the old skill is overwritten
            for key, value in player1.skills_owned.items():
                if value[skilltype] == all_skills[new_buy][skilltype]:
                    del player1.skills_owned[key]
            player1.skills_owned[new_buy] = all_skills[new_buy]
            print "You acquired: ", all_skills[new_buy][title]

        return 'new_level'
# ////////////////////////////////////////////////////////////////////////////////
# ////////////////////////////////////////////////////////////////////////////////
# ////////////////////////////////////////////////////////////////////////////////

class Engine(object):

    def __init__(self, scene_map2):
        self.scene_map = scene_map2

    def play(self): # scene_map is a Map object
        # scene_map.opening_scene() is Map.opening_scene()
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        # be sure to print out the last scene
        current_scene.enter()

class Victory(Scene):

    def enter(self):
        global player1
        toolz.dump_all(player1.hand, player1.discard)
        toolz.transfer_random(player1.discard, player1.deck, len(player1.discard))
        print "Final Deck: ", player1.deck
        print "Final skills: ", list(player1.skills_owned.keys())
        print "You won! Good job."
        return 'finished'

class Death(Scene):

    quips = [
        "You died.  You kinda suck at this.",
        "Your mom would be proud...if she were smarter.",
        "Such a luser.",
        "I have a small puppy that's better at this."
    ]

    def enter(self):

        toolz.dump_all(player1.hand, player1.discard)
        toolz.dump_all(player1.discard, player1.deck)
        print "Highest Level Reached: ", player1.current_level
        # start_menu.print_health(player1.health, "1")
        print "deck:    ", str(len(player1.deck))+"x", "cards", player1.deck
        # return 'death'

        print Death.quips[randint(0, len(self.quips)-1)]
        exit(1)


class Map(object):

    scenes = {
        # 'red_room': RedRoom(),
        # 'blue_room': BlueRoom(),
        # 'yellow_room': YellowRoom(),
        'start_menu': StartMenu(),
        'new_level': New_Level(),

        'fight': Level_Setup("FIGHT"),
        'store': Level_Setup("STORE"),
        'start_printing': Print_Screen_Part(),
        # 'fight': Fight_Level_Battle(),

        'fight_input': Get_Fight_Input(),
        'store_input': Get_Store_Input(),

        'red_room': Fight_Level_Battle("red"),
        'blue_room': Fight_Level_Battle("blue"),
        'yellow_room': Fight_Level_Battle("yellow"),
        # 'pre-death': EndBriefing(),

        # 'store2': Print_Store_Part(),
        'death': Death(),
        'finished': Victory(),
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)

    
if __name__ == "__main__":
    player1 = player_class.player_template()
    world1 = world_template()

    a_map = Map('start_menu')
    # a_map = Map('fight')
    # a_map = Map('central_corridor')
    a_game = Engine(a_map)
    a_game.play()
