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
from other_area import *
import storez


def get_store_instant(new_buy, s_instants_att, player):
    # global player_health
    # print player_health
    if new_buy == "medic":
        # player_health += 3
        player["health"] += 3
    # print player["health"]
