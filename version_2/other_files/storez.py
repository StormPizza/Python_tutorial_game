from sys import exit
from random import randint
import enemies
import math
import time
from settings import *
import toolz



def forced_cycle(player1):
    toolz.dump_all(player1.hand, player1.discard)
    toolz.dump_all(player1.discard, player1.deck)
    player1.draw_full_hand()

    print arrow, "FORCED CYCLE!!! All cards returned to deck, (-1) health"
    player1.take_damage(1)
    player1.calculate_total_power()
    # return player


def bloodlust(player1):
    player1.take_damage(1)
    player1.add_current_effect("bloodlust")
    print arrow, "BLOODLUST! lost (-1) hp, gain <+10> Power this turn only"


def get_store_instant(new_buy, s_instants_att, player1):
    if new_buy == "medic":
        player1.health += all_skills[new_buy][ef_value][0]
