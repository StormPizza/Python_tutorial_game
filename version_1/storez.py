from sys import exit
from random import randint
import enemies
import math
import time
from settings import *
import toolz



def forced_cycle(player):
    # global player_mana
    # if player[player_mana] <= 0:
    #     print arrow, "Not enough mana to use Forced Cycle"
    #     return
    # print dashes, "FORCED CYCLE!!!"
    toolz.dump_all(player[hand], player[discard])
    toolz.dump_all(player[discard], player[deck])
    toolz.draw_full_hand(player)
    # player_mana -= 1

    print arrow, "FORCED CYCLE!!! All cards returned to deck, (-1) health"
    player[health] = toolz.take_damage(player[health], 1)
    player = toolz.set_total_power(player, skills_owned)
    # player[power] = toolz.get_hand_power(player)
    return player

# def blood_lust()

def bloodlust(player):
    player[health] = toolz.take_damage(player[health], 1)
    # toolz.add_effect_to_power(player, "bloodlust")
    # print player[health], "bloodlust"
    player[current_effects] = toolz.add_current_effect(player, "bloodlust")
    print arrow, "BLOODLUST! lost (-1) hp, gain <+10> Power this turn only"
    return player

# This removes any temporary buffs
def get_passive_power(skills_owned, player, world):
    for key, value in skills_owned.items():
        if skills_owned[key][skilltype] == "Passive":
            if key == "half_sharp":
                player[perm_bonus_power] += all_skills[key][ef_value][1]
            elif key == "sharpened":
                player[perm_bonus_power] += all_skills[key][ef_value][1]
            elif key =="double_power":
                player[card_effect] = "double_power"
        # if all_skills[new_buy][skilltype] != "Passive":
            # return
    return player[perm_bonus_power]

# def double_power(player):


def get_store_instant(new_buy, s_instants_att, player):
    # global player_health
    # print player_health
    if new_buy == "medic":
        # player_health += 3
        player["health"] += all_skills[new_buy][ef_value][0]
    # print player["health"]
