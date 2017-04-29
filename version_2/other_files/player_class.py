
from settings import *
import toolz
import storez
# import

class player_template(object):

    def __init__(self):
        player_template.health = 7
        player_template.deck = [0, 0, 0, 1, 1, 1, 1, 1, 1, 1]
        player_template.hand = []
        player_template.discard = []
        player_template.power = 0  # power = card_power + bonus_power
        # power = card_power + perm_ bonus_power + temp_bonus_power
        player_template.card_power = 0
        player_template.player_mana = 3
        player_template.bonus_power = 0  # bonus_power = perm_bonus_power + temp_bonus_power
        player_template.perm_bonus_power = 0

        player_template.status = "alive"  # If Dead, the game ends
        player_template.current_effects = {}  # Current passive and active effects
        # Sample current_effects=
        #     current_effects = {bloodlust= 4, sharpened= 1}
        #     4x instances of bloodlust and 1x passive ability of sharpened

        player_template.card_effect = ""
        player_template.skills_owned = {}


# /////////////////////////////////////////////////////////////////////////////
#     POWER   /  TOTAL HAND POWER   //////////////////////////////////////////

    def set_temp_bonus_power(self):  # checks current effects and applies stats
        self.temp_bonus_power = 0
        # print self.current_effects
        for key, value in self.current_effects.items():
            effects_no = self.current_effects[key]
            # Get effect value from all_skills library
            if all_skills[key][skilltype] != "Passive":  # Passives are not temp
                self.temp_bonus_power += all_skills[key][ef_value][1] * effects_no
            elif key == "double_power":
                self.temp_bonus_power += all_skills[key][ef_value][1] * effects_no
        return self.temp_bonus_power

    def set_perm_bonus_power(self):  # Resets stats down to minimum
        self.perm_bonus_power = 0  # If no passive effects are found
        # for key, value in self.skills_owned.items():
        for key, value in self.current_effects.items():
            if all_skills[key][skilltype] == "Passive":
                self.perm_bonus_power = self.get_passive_power()
        return self.perm_bonus_power

    def set_bonus_power(self):  # from all current_effects
        self.bonus_power = 0
        self.bonus_power += self.set_perm_bonus_power()
        self.bonus_power += self.set_temp_bonus_power()
        return self.bonus_power

    def get_card_power(self):  # Calc total power from 5 cards in hand
        # INPUT player class, add each item in list, one at a time
        self.card_power = reduce(lambda x, y: x+y, self.hand)
        return self.card_power

    def calculate_total_power(self):
        if len(self.hand) == 0:
            return None
        # self.power = 0
        # self.power += get_card_power(player)
        # self.power += set_bonus_power(player)
        self.power = self.get_card_power() + self.set_bonus_power()


# //////////////////////////////////////////////////////////////////////////
# //    CURRENT EFFECTS    /////////////////////////////////////////////////

    def add_current_effect(self, skill_name):
        # INPUT: skill_name and player.current_effects
        # If skill_name is in current effects, increment stack by 1
        # If not, add to list of active effects
        self.current_effects[skill_name] = self.current_effects.setdefault(skill_name, 0)+1
        # if skill_name in self.current_effects:
        #     self.current_effects[skill_name] += 1
        # else:
        #     self.current_effects[skill_name] = 1
        # return self.current_effects

    def set_effects_from_draw(self, passive_name):  # double_power
        for key, value in self.current_effects.items():
            if all_skills[key][trigger] == "from_hand":
                del self.current_effects[key]
        # hand_bonus = 0  # this can be zeroed
        # Check for double_power   ////////////////////////
        count_list = {}  # count how many of each card there are in hand
        for i in self.hand:
            # if i in count_list:
            #     count_list[i] += 1
            # else:
            #     count_list[i] = 1
            count_list[i] = count_list.setdefault(i, 0)+1
        # count_list = { 0:2, 1:3 }
        for key, value in count_list.items():  # Apply double_power - only if applicable
            if count_list[key] > 1 and key > 0:
                self.add_current_effect(passive_name)
        return self.current_effects

    # This removes any temporary buffs
    def get_passive_power(self):
        for key, value in self.skills_owned.items():
        # for key, value in self.current_effects.items():
            if self.skills_owned[key][skilltype] == "Passive":
                if key == "half_sharp":
                    self.perm_bonus_power += all_skills[key][ef_value][1]
                elif key == "sharpened":
                    self.perm_bonus_power += all_skills[key][ef_value][1]
                elif key == "double_power":
                    self.card_effect = "double_power"
            # if all_skills[new_buy][skilltype] != "Passive":
                # return
        return self.perm_bonus_power


# /////////////////////////////////////////////////////////////////////////////
#       HP   and    DAMAGE       //////////////////////////////////////////////

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            print " \n You Died."
            exit(1)
            # return 'death'
        # text_take_damage(player_health, damage)
        # return player_health

    def text_take_damage(self, damage):
        print arrow, "Unfortunately you take %d damage" % damage
        print arrow, "Player_health: %d ---" % self.health, "H " * self.health

# /////////////////////////////////////////////////////////////////////////////
#     CARDS      //////////////////////////////////////////////////////////////

    def draw_full_hand(self):
        if len(self.deck) < 5:     # draw up to 5 cards if possible
            if len(self.discard) < 5:
                self.status = "dead"
            toolz.transfer_random(self.deck, self.hand, len(self.deck))
            toolz.transfer_random(self.discard, self.deck, len(self.discard))
        toolz.transfer_random(self.deck, self.hand, 5-len(self.hand))
        # Check for auto-trigger skills
        for key, value in self.skills_owned.items():  # Passive, but auto-trigger
            if key == "double_power":
                self.current_effects = self.set_effects_from_draw("double_power")

        #     transfer_random(self.deck, self.hand, len(self.deck))
        #     transfer_random(self.discard, self.deck, len(self.discard))
        # transfer_random(self.deck, self.hand, 5-len(self.hand))

    def dump_hand(self):
        toolz.transfer_random(self.hand, self.discard, len(self.hand))
