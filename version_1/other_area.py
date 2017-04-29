from sys import exit
from random import randint
from ex45_raw import *
import toolz
import format_display
# To keep dictionaries in the order they were made
# from collections import OrderedDict
import math
import os
from settings import *
# from ex45 import *


# class Storefront(Scene):  # This is the main room where decisions will be made
#
#     def enter(self):
#         global current_level, final_note, store_count
#         global deck, hand, discard, power
#         global dashes, spaces5
#
#         # ------------------SETUP - TITLE OF CURRENT ROOM
#         format_display.print_level_bar("STORE", player_health, final_note)
#
#         # ------------------Display current deck and discard
#         toolz.dump_hand(hand, discard)
#         # toolz.starting_phase(deck, hand, discard)
#         toolz.print_card_stats(deck, hand, discard, "nodraw")
#         action1 = raw_input("Select a room(q,w,e,r): ").lower()
#
#         print "store", store_count
#         store_count += 1
#         print "store", store_count
#         return 'choice'
