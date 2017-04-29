# from key_words import *
# KEYWORDS
health = "health"
deck = "deck"
hand = "hand"
discard = "discard"
power = "power"
mana = "mana"
bonus_power = "bonus_power"
status = "status"
current_effects = "current_effects"
perm_power = "perm_power"
card_power = "card_power"
perm_bonus_power = "perm_bonus_power"
temp_bonus_power = "temp_bonus_power"
card_effect = "card_effect"
option_order = "option_order"
option_freq = "option_freq"

store_open = "store_open"
current_level = "current_level"
max_level = "max_level"
final_note = "final_note"
player_mana = "player_mana"
store_interval = "store_interval"

effect_target = "effect_target"
ef_value = "ef_value"
onplayer = "onplayer"
onworld = "onworld"
trigger = "trigger"
from_hand = "from_hand"

title = 'title'
desc = 'desc'
skilltype = 'type'
code = "code"


class world_template(object):
    def __init__(self):
        world_template.current_level = 0
        world_template.max_level = 50
        world_template.final_note = ""
        world_template.store_interval = 5
        world_template.room_desc_interval = 5
        world_template.level_type = "we_be_fighting"

    # see http://bit.ly/2ox7wmY
    def printName():
        return str(__name__)

# world1 = world_template()

# MONSTER STATS
red_monster = 0
blue_monster = 0
yellow_monster = 0


# TOGGLE
# final_note = ""

# Typography
# dashes = "///////////////////////////////////////////////////////"
DASHES = "/" * 55
SCREEN_LENGTH = 75
SHORT_DASHES = "////////"
margin = "   "
arrow = "---------------->>"
spaces5 = "     "

# FORMAT DISPLAY CONSTANTS
ROOMS_NO = 3
OPTIONS_NO = 1
RM_SKILLS_NO = 1

LIST_ORDER = ["q", "w", "e", "r", "a"]

MAXLEN = "Foe Power: 100"
TEXTLEN = len(MAXLEN)
# ////////////////   ROOM   ///////////////////////////////////////////

# class Level_Choices(object):
#     def __init__(self):
#         self.title = ""  # Red Room, Blue Room, Yellow Room
#         self.desc = ""
#         self.skilltype = ""  # Monster, Active, Passive
#         self.effect_target = ""
#         self.trigger = ""
#         self.ef_value = [0, 0]  # [  (+/-HP)  (+/-Power) ]
#         self.code = ""  # q, w, e, r, a
#
# new_thing = "red_room"
# exec(str(new_thing) + " = Level_Choices()")
# exec(str(new_thing) + ".title = \"%s\"" % "Red Room")
# exec(str(new_thing) + ".skilltype = \"%s\"" % "Monster")
# exec(str(new_thing) + ".code = \"%s\"" % "q")
#
# new_thing = "blue_room"
# exec(str(new_thing) + " = Level_Choices()")
# exec(str(new_thing) + ".title = \"%s\"" % "Blue Room")
# exec(str(new_thing) + ".skilltype = \"%s\"" % "Monster")
# exec(str(new_thing) + ".code = \"%s\"" % "w")
#
# new_thing = "yellow_room"
# exec(str(new_thing) + " = Level_Choices()")
# exec(str(new_thing) + ".title = \"%s\"" % "Yellow Room")
# exec(str(new_thing) + ".skilltype = \"%s\"" % "Monster")
# exec(str(new_thing) + ".code = \"%s\"" % "e")
#
# new_thing = "skip"
# exec(str(new_thing) + " = Level_Choices()")
# exec(str(new_thing) + ".title = \"%s\"" % "Skip")
#
# room_list = {
#     "red_room": red_room,
#     "blue_room": blue_room,
#     "yellow_room": yellow_room
# }
option_order = "option_order"
option_freq = "option_freq"

red_room = {
    title: "Red Room",
    desc: "",
    skilltype: "Monster",
    effect_target: "",
    trigger: "",
    ef_value:  [0, 0],
    code: "q",
    option_order: 1,
    option_freq: "ALWAYS"
}

blue_room = {
    title: "Blue Room",
    desc: "",
    skilltype: "Monster",
    effect_target: "",
    trigger: "",
    ef_value:  [0, 0],
    code: "w",
    option_order: 2,
    option_freq: "ALWAYS"
}

yellow_room = {
    title: "Yellow Room",
    desc: "",
    skilltype: "Monster",
    effect_target: "",
    trigger: "",
    ef_value:  [0, 0],
    code: "e",
    option_order: 3,
    option_freq: "ALWAYS"
}

rooms_dict = {
    "red_room": red_room,
    "blue_room": blue_room,
    "yellow_room": yellow_room
}



skip = {
    title: "Skip",
    desc: "",
    skilltype: "",
    effect_target: "",
    trigger: "",
    ef_value:  [0, 0],
    code: "",
    option_order: 4,
    option_freq: "ALWAYS"
}

other_dict = {
    "Skip": skip
}

all_room_option_list = {}
all_room_option_list.update(rooms_dict)
all_room_option_list.update(other_dict)

room_list = list(rooms_dict)
other_list = list(other_dict)

# ////////////////   SKILLS   ///////////////////////////////////////////
# Distribution of skills available in store
active_no = 2
passive_no = 2
instant_no = 1

# new_thing = "forced_cycle"
# exec(str(new_thing) + " = Level_Choices()")
# exec(str(new_thing) + ".title = \"%s\"" % "Forced Cycle")
# exec(str(new_thing) + ".desc = \"%s\"" % "Return all   cards to the deck")
# exec(str(new_thing) + ".skilltype = \"%s\"" % "Active")
# exec(str(new_thing) + ".effect_target = \"%s\"" % "onplayer")
# new_thing = "bloodlust"
# exec(str(new_thing) + " = Level_Choices()")
# exec(str(new_thing) + ".title = \"%s\"" % "Bloodlust")
# exec(str(new_thing) + ".desc = \"%s\"" % "Lose (1) hp  to gain <+10> power  this turn")
# exec(str(new_thing) + ".skilltype = \"%s\"" % "Active")
# exec(str(new_thing) + ".effect_target = \"%s\"" % "onplayer")
# exec(str(new_thing) + ".ef_value = \"%s\"" % "[-1, +10]")
# new_thing = "sharpened"
# exec(str(new_thing) + " = Level_Choices()")
# exec(str(new_thing) + ".title = \"%s\"" %  "Sharpened")
# exec(str(new_thing) + ".desc = \"%s\"" % "Permanently  gain <+5>    power")
# exec(str(new_thing) + ".skilltype = \"%s\"" % "Passive")
# exec(str(new_thing) + ".effect_target = \"%s\"" % "onplayer")
# exec(str(new_thing) + ".ef_value = \"%s\"" % "[0, +5]")
# new_thing = "half_sharp"
# exec(str(new_thing) + " = Level_Choices()")
# exec(str(new_thing) + ".title = \"%s\"" % "Half Sharp")
# exec(str(new_thing) + ".desc = \"%s\"" % "Permanently  gain <+2>    power")
# exec(str(new_thing) + ".skilltype = \"%s\"" % "Passive")
# exec(str(new_thing) + ".effect_target = \"%s\"" % "onplayer")
# exec(str(new_thing) + ".ef_value = \"%s\"" % "[0, +2]")
# new_thing = "double_power"
# exec(str(new_thing) + " = Level_Choices()")
# exec(str(new_thing) + ".title = \"%s\"" % "Double Power")
# exec(str(new_thing) + ".desc = \"%s\"" % "Pairs in hand give <+5>   power")
# exec(str(new_thing) + ".skilltype = \"%s\"" % "Passive")
# exec(str(new_thing) + ".effect_target = \"%s\"" % "onplayer")
# exec(str(new_thing) + ".trigger = \"%s\"" % "from_hand")
# exec(str(new_thing) + ".ef_value = \"%s\"" % "[0, +5]")
# new_thing = "medic"
# exec(str(new_thing) + " = Level_Choices()")
# exec(str(new_thing) + ".title = \"%s\"" % "Medic")
# exec(str(new_thing) + ".desc = \"%s\"" % "Gain (2) hp  immediately")
# exec(str(new_thing) + ".skilltype = \"%s\"" % "Instant")
# exec(str(new_thing) + ".effect_target = \"%s\"" % "onplayer")
# exec(str(new_thing) + ".ef_value = \"%s\"" % "[+2, 0]")

forced_cycle = {
    title: "Forced Cycle",
    desc: "Return all   cards to the deck",
    skilltype: "Active",
    effect_target: onplayer,
    trigger: "",
    ef_value: [0, 0],
    code: "",
    option_order: "",
    option_freq: ""
}

bloodlust = {
    title: "Bloodlust",
    desc: "Lose (1) hp  to gain <+10> power  this turn",
    skilltype: "Active",
    effect_target: onplayer,
    trigger: "",
    ef_value: [-1, +10],
    code: "",
    option_order: "",
    option_freq: ""
}

sharpened = {
    title: "Sharpened",
    desc: "Permanently  gain <+5>    power",
    skilltype: "Passive",
    effect_target: onplayer,
    trigger: "",
    ef_value: [0, +5],
    code: "",
    option_order: "",
    option_freq: ""
}

half_sharp = {
    title: "Half Sharp",
    desc: "Permanently  gain <+2>    power",
    skilltype: "Passive",
    effect_target: onplayer,
    trigger: "",
    ef_value: [0, +2],
    code: "",
    option_order: "",
    option_freq: ""
}

double_power = {
    title: "Double Power",
    desc: "Pairs in hand give <+5>   power",
    skilltype: "Passive",
    effect_target: onplayer,
    trigger: from_hand,
    ef_value: [0, +5],
    code: "",
    option_order: "",
    option_freq: ""
}

medic = {
    title: "Medic",
    desc: "Gain (2) hp  immediately",
    skilltype: "Instant",
    effect_target: onplayer,
    trigger: "",
    ef_value: [+2, 0],
    code: "",
    option_order: "",
    option_freq: ""
}

# ////////  SKILLS COMPILED ///////////////////////

a_skills = {
    "forced_cycle": forced_cycle,
    "bloodlust": bloodlust
}

p_skills = {
    "double_power": double_power,
    "sharpened": sharpened,
    "half_sharp": half_sharp
}

s_instants = {
    "medic": medic
}

# //////////////////////////////////////////////////////////
all_skills = {}
all_skills.update(a_skills)
all_skills.update(p_skills)
all_skills.update(s_instants)

active_list = list(a_skills)
passive_list = list(p_skills)
instant_list = list(s_instants)

EVERYTHING_LIBRARY = {}
EVERYTHING_LIBRARY.update(all_skills)
EVERYTHING_LIBRARY.update(all_room_option_list)
