import time, math, copy, random
from prettytable import PrettyTable
from PyInquirer import prompt
from importlib import reload
from Functions import char_creation, choose_moves, ready_up, turn_tracker, print_stat_table, total_turns,\
    log_sign_choice, actions_log, choose_new_attack

from Item import HealthItem, DefensiveItem, TurnCreditBoostItem, ReviveItem
from Actions import Action, FireAction, TechAction, WaterAction, EarthAction, TelepathAction, ProtectorAction
from Heros import Hero, ShamanHero, FireWarlockHero, TechromancerHero \
    , WaterEnchanterHero, EarthOperatorHero, TelepathHero, ShamanHero, BioHero
from Villians import Villain, ShamanVillain, FireWarlockVillain, TechromancerVillain \
    , WaterEnchanterVillain, EarthOperatorVillain, TelepathVillain, ShamanVillain, BioVillain

from tkinter import *
# _+_+_+_+_+_+_+_+_+_+_+_+ TO DO _+_+_+_+_+_+_+_+_+_+_



# still need to find a way to make the amount healed a random number every time

# add additional levels (Preferably 5 more)


# "Miss!" not printing during battle randomly

# remove quotes around Moves in PrettyTable


# _+_+_+_+_+_+_+_+_+_+_+_+ DONE +_+_+_+_+_+_+_+_+_+_+_+_+
# def add_health() created working
# heal working on villain and hero
# check_health() built and updated
# no longer can over heal
# when healing at close to full health, "regained health" accounts for the max health limit
# make potions use able

# Items classes init, 3 potion objects created
# def add_potion() created
# Potions are no longer usable with no uses
# heroes and villains given "items" instance = []
# options_screen() created and working < allows choices to attack or use an item

# no longer able to choose an attack with no uses left after trying to heal at full health
# attack works after trying tu use a potion at full health

# moves added
# check_uses() built and working for hero and villain
# player attack pulled out of battle and made into own function = get_player_attack()
# initialization for Action now includes a type attribute/instance
# second moves list added for later when editing attacks will be init
# allowed players to choose new move later on in the game
# show moves table before every choice of attack

# made villains choose new move when healing at full health
# don't let villains heal when already at full health

# in battle(193, 194) hp is hard set this needs to be dynamic

# make "are you ready" input = PyInquirer

# moves added to list dynamically not independently
# randomized chosen villain attacks
# hero and villain no longer deducting uses from the same move object
# < resolved by deepcopy() the "move" object and THEN adding it to the hero or villain object
# changed add_move to move_list to be dynamic and add moves to multiple lists


# IN ACTIONS fire, tech, water, earth, telepath and protector subclasses built
# IN ITEM health, defensive, turn credit boost and, revive subclasses built
# IN heroes FireWarlock, Techromancer, WaterEnchanter, Earth_Operator, Telepath and Protector subclasses built

# _+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_  LIST'S _+_+_+_+_+_+_+_+_+_+_+_+_
villain_list = []
hero_list = []
starting_moves = []
later_moves = []
high_scores = []
# _+_+_+_+_+_+_+_+_+_+_+_+_+_+ FUNCTIONS +_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_


def add_move_to_moves_list(move_list, move_object):
    move_list.append(move_object)


def add_villian_to_villain_list(villain):
    villain_list.append(villain)


def get_rand_int(x, y):
    new_num = int(random.randint(x, y))
    return new_num


def add_villain_moves(villain, moves):
    move_choices = random.sample(moves, 4)
    for move in move_choices:
        copied_move = copy.deepcopy(move)
        villain.add_move(copied_move)


def add_potion(current_hero, item):
    copied_item = copy.deepcopy(item)
    current_hero.items.append(copied_item)


def get_score(time_taken, final_hero_health, hero_name):
    from Functions import ALL_TURNS
    score = int(final_hero_health * (time_taken / ALL_TURNS))
    print(f"\nYou're final score is {score}")
    high_scores.append((hero_name, score))
    score_board(high_scores)
    return score


def score_board(score_list):
    sb = PrettyTable()
    sb.field_names = ["Name", "High Score"]
    for i in score_list:
        sb.add_row([i[0], i[1]])
    print(sb)


def play_again():
    questions = [
        {
            "type": "checkbox",
            "message": "Play again?",
            "name": "choice",
            "choices": [
                {
                    'name': "Yes"
                },
                {
                    'name': "No"
                }
            ]
        }
    ]

    answer = prompt.prompt(questions)
    coded_answer = ""

    for i in answer["choice"]:
        coded_answer = str(i)

    if coded_answer == "Yes":
        for i in villain_list:
            i.hp = i.max_hp
            for n in i.attack:
                n.uses = n.max_uses
        for i in hero_list:
            for n in i.attack:
                n.uses = n.max_uses
        print("got here")
        core_game(villain_list)
    else:
        print("Game exited")


# _+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+ ITEMS STUFF_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+


weak_potion = HealthItem("Weak Potion", 1, "Health Potion", 10)
mild_potion = HealthItem("Mild Potion", 1, "Health Potion", 20)
strong_potion = HealthItem("Strong Potion", 1, "Health Potion", 30)

# _+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+ MOVES STUFF_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+


punch = Action("Punch", 25, 25, 10, "Melee")
add_move_to_moves_list(starting_moves, punch)

kick = Action("Kick", 22, 22, 13, "Melee")
add_move_to_moves_list(starting_moves, kick)

slam = Action("Slam", 19, 19, 16, "Melee")
add_move_to_moves_list(starting_moves, slam)

smash = Action("Smash", 16, 16, 19, "Melee")
add_move_to_moves_list(starting_moves, smash)

clober = Action("Clober", 13, 13, 22, "Melee")
add_move_to_moves_list(starting_moves, clober)

blast_blitz = Action("Blast Blitz", 10, 10, 25, "Melee")
add_move_to_moves_list(starting_moves, blast_blitz)

atomic_charge = Action("Atomic Charge", 1, 1, 35, "Melee")
add_move_to_moves_list(starting_moves, atomic_charge)

heal = ProtectorAction("Heal", 10, 10,  "15", "Healing", 20)
add_move_to_moves_list(starting_moves, heal)

super_heal = ProtectorAction("Super Heal", 6, 6, "25", "Healing", 25)
add_move_to_moves_list(later_moves, super_heal)

holy_heal = ProtectorAction("Holy Heal", 1, 1, "500", "Healing", 500)
add_move_to_moves_list(later_moves, holy_heal)

# +_+_+_+_+_+_+_+_+_+_+_+_+_+_+_ HEROS _+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+
# add heroes here
blaze = FireWarlockHero("Blaze", 100, 100, 65, 10, 10)

# _+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_ VILLIANS _+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+

heat_monger = FireWarlockVillain("Heat Monger", 10, 80, 0, 0, 0)
add_villian_to_villain_list(heat_monger)
add_villain_moves(heat_monger, starting_moves)

maganox = TechromancerVillain("Maganox", 10, 80, 0, 0, 0)
add_villian_to_villain_list(maganox)
add_villain_moves(maganox, starting_moves)

heshera = WaterEnchanterVillain("Heshera", 10, 100, 0, 0, 0)
add_villian_to_villain_list(heshera)
add_villain_moves(heshera, starting_moves)

brim = EarthOperatorVillain("Brim", 100, 100, 0, 0, 0)
#add_villian_to_villain_list(brim)
add_villain_moves(brim, starting_moves)

eskel = TelepathVillain("Eskel", 100, 100, 0, 0, 0)
#add_villian_to_villain_list(eskel)
add_villain_moves(eskel, starting_moves)

dr_toxic = BioVillain("Dr.Toxic", 100, 100, 0, 0, 0)
#add_villian_to_villain_list(dr_toxic)
add_villain_moves(dr_toxic, starting_moves)

# _+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+ CALLER CODE +_+_+_+_+_+_+_+_+_+_+_+_+_+_+



def core_game(vill_list):

    level = 0
    seen_level = 1
    print("Welcome to The Tower...Good luck getting to the top...You're going to need it...")
    our_hero = Hero(char_creation(), 500, 500, 60)
    hero_list.append(our_hero)
    our_hero.add_potion(weak_potion)
    choose_moves(our_hero, starting_moves)
    if ready_up(our_hero, villain_list[level]):

        while level < len(villain_list):
            from Functions import actions_log
            start_time = time.time()
            actions_log.append({"level": seen_level})
            if turn_tracker(our_hero, villain_list[level]) != True and level < len(villain_list):
                seen_level += 1
                level += 1
                if level == 1 or level == 2:
                    choose_new_attack(our_hero, later_moves)
                if level >= len(villain_list):
                    end_time = time.time()
                    total_time = end_time - start_time
                    print(f"our heros health is now at {our_hero.hp}")
                    print("\n\nGAME BEAT, YOU DID IT!!")
                    get_score(total_time, our_hero.hp, our_hero.name)
                else:
                    print(f"\n\n\nThy next foe is none other that the great {villain_list[level].name}!!")
                    print_stat_table(our_hero, villain_list[level])

            from Functions import ALL_TURNS
            actions_log.append({"Total Turns": ALL_TURNS})
        if level == len(villain_list):
            pass


            #play_again()



log_sign_choice()
core_game(villain_list)




#print(high_scores[0][1])
#print(actions_log)