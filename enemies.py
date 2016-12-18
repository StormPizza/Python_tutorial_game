
from random import randint

def enemy_generator():

    adjective = [
        "COOL-HEADED",
        "UNPREDICTABLE",
        "CRABBY",
        "BITCHY",
        "FEARLESS",
        "GENTLE",
        "CONFIDENT",
        "OUTGOING",
        "RESPECTFUL",
        "BLUNT",
        "IRRITABLE",
        "AMBITIOUS",
        "THOUGHTFUL",
        "EAGER",
        "EXCITABLE",
        "INSENSITIVE",
        "HYPERCRITICAL",
        "DECISIVE",
        "EASY-GOING",
        "ANXIOUS",
        "UNBALANCED",
        "DISGRACED",
        "TACTLESS",
    ]

    race = [
        "GNOME",
        "ELF",
        "HALF-ORC",
        "GNOME",
        "DWARF",
        "DRAGONBORN",
        "TIEFLING",
        "HALFLING"
    ]
    occupation = [
        "ROGUE",
        "WIZARD",
        "BARBARIAN",
        "SORCERER",
        "BARD",
        "RANGER",
        "MONK",
        "DRUID",
        "FIGHTER",
        "PALADIN",
        "WARLOCK",
        "CLERIC"
    ]
    land = [
        "FROM THE CITY SLUMS",
        "FROM A QUAINT LITTLE VILLAGE ON A HILL",
        "FROM THE NORTHERN ICELANDS",
        "FROM A DYSFUNCTIONAL MARRIAGE",
        "FROM A HIGH END GAMBLING HOUSE",
        "FROM A CITY IN THE SHIFTING SANDS",
        "FROM A SECLUDED FOREST VILLAGE",
        "FROM THE ENDLESS WASTES",
        "WHO IS REALLY (I MEAN REALLY) AFRAID OF THE DARK",
        "FROM A DISGRACED FAMILY OF KNIGHTS",
        "FROM A BOARDING SCHOOL FOR THE CHILDREN OF MIDDLE-CLASS WIZARDS",
        "FROM THE DUSTY MOUNTAINS",
        "FROM A SLAVE CARAVAN",
        "FROM AN INTERNMENT CAMP",
        "FROM A CAVERN WITHOUT ECHOES",
        "FROM A TOWN THAT ONLY EVER BARTERED FOR GOODS",
        "FROM AN INTERNMENT CAMP",
        "FROM THE DUNGEON INSPECTOR'S GUILD (LOCAL #422)",
        "FROM THE STRONGEST FAMILY HERITAGE LINE IN THE LAND",
        "FROM AN UNDERGROUND CITY",
        "FROM THE RAT CATCHERS GUILD",
        "FROM A RECENTLY ERUPTED VOLCANO VILLAGE "
    ]

    who = [
        "WHO REJECTED A FOREIGN PRINCE'S MARRIAGE PROPOSAL",
        "WHO HAS NO CONCEPT OF PERSONAL SPACE",
        "WHO IS CURRENTLY ON PROBATION FOR DRUNK AND DISORDERLY BEHAVIOUR",
        "WHO IS THE TWIN OF THE LOCAL MONARCH",
        "WHO OPENS A NEW BAG OF CHIPS WITHOUT FINISHING THE OLD ONE",
        "WHO HAS A PRETTY SELECTIVE MEMORY",
        "WHO IS THE SPITTING IMAGE OF A KOALA",
        "WHO IS AFRAID OF HEIGHTS",
        "WHO CONSTANTLY WATCHES THEIR BACK",
        "WHO MAKES INAPPROPRIATE JOKES AT THE WORST TIMES",
        "WHO IS EXTREMELY FRUSTRATED THAT HIS SOCKS DON'T MATCH",
        "WHO CARRIES AROUND A DREAM JOURNAL",
        "WHO HAS TWENTY-SEVEN SIBLINGS TO PROVIDE FOR",
        "WHO REALISED THE IMPORTANCE OF LITERACY FAR TOO LATE IN LIFE",
        "WHO ONLY NOW JUST REALISED THAT HE LEFT THE STOVE ON",
        "WHO INSISTS THEY ARE THE REINCARNATION OF A LEGENDARY WARRIOR",
        "WHO WAS BORN IN A DIFFERENT BODY",
        "WHO NEVER RETURNED ANYTHING THEY BORROWED",
        "WHO IS SEARCHING FOR A RARE FERTILITY HERB",
        "WHO WANTS EVERYONE TO LIKE THEM",
        "WHO CONVINCED THAT WEARING PANTS IMPEDES HIS FIGHTING ABILITY",
        "WHO SUFFERS FROM A RECURRING NIGHTMARE",
        "WHO ALWAYS GIVES THE BAD NEWS FIRST"
    ]

    part1 = adjective[randint(0, len(adjective)-1)]
    part2 = race[randint(0, len(race)-1)]
    part3 = occupation[randint(0, len(occupation)-1)]
    part4 = land[randint(0, len(land)-1)]
    part5 = who[randint(0, len(who)-1)]
    # print part1, part2, part3
    # esd = part1 + part2
    # print esd
    enemy = part1 + " " + part2 + " " + part3 + " " + part4 + " " + part5
    return enemy
