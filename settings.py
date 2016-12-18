from key_words import *
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



player = {
    "health": 7,
    "deck": [0, 0, 0, 1, 1, 1, 1, 1, 1, 1],
    "hand": [],
    "discard": [],
    "power": 0,  # power = card_power + bonus_power
                 # power = card_power + perm_ bonus_power + temp_bonus_power
    "card_power": 0,
    "player_mana": 3,
    "bonus_power": 0,  # bonus_power = perm_bonus_power + temp_bonus_power
    "status": "alive",  # If Dead, the game ends
    "current_effects": {},  # Current passive and active effects
    # Sample current_effects:
    #     current_effects = {bloodlust: 4, sharpened: 1}
    #     4x instances of bloodlust and 1x passive ability of sharpened
    "perm_bonus_power": 0,
    "card_effect": ""
}

skills_owned = {}

world = {
    "current_level": 0,
    "max_level": 20,
    "store_open": "closed",
    # TOGGLE
    "final_note": "",
    "store_interval": 5


}

# MONSTER STATS
red_monster = 0
blue_monster = 0
yellow_monster = 0


# TOGGLE
# final_note = ""


# Typography
dashes = "///////////////////////////////////////////////////////"
short_dashes = "////////"
margin = "   "
arrow = "---------------->>"
spaces5 = "     "


rooms_no = 3
options_no = 1
rm_skills_no = 1

list_order = ["q", "w", "e", "r", "a"]

maxlen = "Foe Power: 100"

# ////////////////   ROOM   ///////////////////////////////////////////

red_room = {
    title: "Red Room",
    desc: "",
    skilltype: "Monster",
    effect_target: "",
    trigger: "",
    ef_value:  [0, 0],
    code: "q"
}

blue_room = {
    title: "Blue Room",
    desc: "",
    skilltype: "Monster",
    effect_target: "",
    trigger: "",
    ef_value:  [0, 0],
    code: "w"
}

yellow_room = {
    title: "Yellow Room",
    desc: "",
    skilltype: "Monster",
    effect_target: "",
    trigger: "",
    ef_value:  [0, 0],
    code: "e"
}

room_list = {
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
    ef_value:  [0, 0]
}

option_list = {
    "Skip": skip
}

# ////////////////   SKILLS   ///////////////////////////////////////////
# Distribution of skills available in store
active_no = 2
passive_no = 2
instant_no = 1

forced_cycle = {
    title: "Forced Cycle",
    desc: "Return all   cards to the deck",
    skilltype: "Active",
    effect_target: onplayer,
    trigger: "",
    ef_value: [0, 0]
}

bloodlust = {
    title: "Bloodlust",
    desc: "Lose (1) hp  to gain <+10> power  this turn",
    skilltype: "Active",
    effect_target: onplayer,
    trigger: "",
    ef_value: [-1, +10]
}

sharpened = {
    title: "Sharpened",
    desc: "Permanently  gain <+5>    power",
    skilltype: "Passive",
    effect_target: onplayer,
    trigger: "",
    ef_value: [0, +5]
}

half_sharp = {
    title: "Half Sharp",
    desc: "Permanently  gain <+2>    power",
    skilltype: "Passive",
    effect_target: onplayer,
    trigger: "",
    ef_value: [0, +2]
}

double_power = {
    title: "Double Power",
    desc: "Pairs in hand give <+5>   power",
    skilltype: "Passive",
    effect_target: onplayer,
    trigger: from_hand,
    ef_value: [0, +5]
}

medic = {
    title: "Medic",
    desc: "Gain (2) hp  immediately",
    skilltype: "Instant",
    effect_target: onplayer,
    trigger: "",
    ef_value: [+2, 0]
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
