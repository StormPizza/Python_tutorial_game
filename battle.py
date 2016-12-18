from sys import exit
from random import randint
import enemies
import math
import time
from settings import *
import storez
import toolz
def lose_fight(player_health):
    # global player_attack, player_health, current_level
    print "--->>The monster defeated you, you lose 1 health"
    player_health = toolz.take_damage(player_health, 1)
    return player_health

def show_fight_text(monster_attack, player_attack):
    enemy_name = enemies.enemy_generator()
    print "You encounter a", enemy_name.lower()
    print "\nPLAYER : You attack with your power of     ", player_attack
    print "MONSTER: You fight a monster with power of ", monster_attack
    # print "\n"

def fight_resolution(player_attack, monster_attack):
        power_gap = abs(monster_attack-player_attack)
        backup_roll = randint(1, power_gap + 2)  #66% for 1, 50% for 2,etc
        if player_attack >= monster_attack:
            # Instant Win
            return "win"
        elif backup_roll <= 2:
            print "\nThe monster has higher power, but you pull through"
            return "half_win"
        else:
            print "You rolled %d when you needed to roll <= 2" % backup_roll
            return 'lose'

def red_prize(current_level, discard):  # Prize for clearing the red room
    print "You defeat the monster\n"
    reward = int(math.ceil(current_level/1.5))  # randint(2,3)
    print arrow, "You gained a new card [%d], added to discard pile" % reward
    discard.append(reward)
    reward_list = []
    reward_list.append(reward)
    reward_text = ", Gained "
    for i in reward_list:
        reward_text += str(reward_list)
    return reward_text

def blue_prize(hand, discard):  # Prize for clearing the blue room
    # Trashes the lowest power card in your hand or discard pile
    # But first checks if the hand of discard is empty
    big_no = 99999999
    if len(hand) == 0:
        min_hand = big_no
    else:
        min_hand = min(hand)
    if len(discard) == 0:
        min_discard = big_no
    else:
        min_discard = min(discard)
    #Then checks if the lowest power card in your hand is lower than discard
    if min_hand < min_discard:
        reward = min(hand)
        remove_place = "hand"
        hand.remove(reward)
    else:
        reward = min(discard)
        remove_place = "discard pile"
        discard.remove(reward)
    print arrow, "You cast away the card [%d], removed from your %s" % (reward, remove_place)

    reward_list = []
    reward_list.append(reward)
    reward_text = ", Trashed "
    for i in reward_list:
        reward_text += str(reward_list)
    return reward_text

def yellow_prize(current_level, discard):  # Prize for clearing the yel room
    reward = int(math.ceil(current_level/3))
    print arrow, "You gained a new card [%d], added to discard pile" % reward
    print arrow, "You gained a new card [%d], added to discard pile" % reward
    print arrow, "You gained a new card [%d], added to discard pile" % reward
    discard.extend([reward, reward, reward])

    reward_list = []
    reward_list.append(reward)
    reward_list.append(reward)
    reward_list.append(reward)
    reward_text = ", Gained "
    for i in reward_list:
        reward_text += str(reward_list)
    return reward_text
