from __future__ import print_function, unicode_literals
import random
from prettytable import PrettyTable
from PyInquirer import prompt, print_json
from Heros import hero_turn_art

# _+_+_+_+_+_+_+_+_+_+_+_+ ART _+_+_+_+_+_+_+_+_+_+_+_+_+





def introduction():
    print("Welcome to The Tower...Good luck getting to the top...Youre going to need it...")


def char_creation():
    return input("What is your name hero?\n")


def choose_moves(our_hero, list_moves):
    #return False
    moves_table = PrettyTable()
    moves_table.field_names = ["Name", "Uses", "Damage"]

    for move in list_moves:
        moves_table.add_row([move.name, move.uses, move.damage])

    print(moves_table)
    chosen = "What 4 moves will you choose? Please separate choices with a comma and a space.\n"
    chosen_moves = chosen.split(", ")

    for c_move in chosen_moves:
        for l_move in list_moves:
            if l_move.name == c_move:
                our_hero.attack.append(l_move)

    choices = []
    for i in list_moves:
        choices.append({"name": i.name})

    questions = [
        {
            "type": "checkbox",
            "message": f"What 4 moves would like to use {our_hero.hero_name}?",
            "name": "move_list",
            "choices": choices
        }
    ]

    answers = prompt.prompt(questions)

    for i in answers["move_list"]:
        our_hero.attack.append(i)

    chosen_moves_table = PrettyTable()
    chosen_moves_table.field_names = ["Name", "Uses", "Damage"]

    counter = 0
    for i in our_hero.attack:
        for obj in list_moves:
            obj_name = str(obj.name)
            if i == obj_name:
                our_hero.attack[counter] = obj
                counter += 1

    for i in our_hero.attack:
        chosen_moves_table.add_row([i.name, i.uses, i.damage])

    print("\nHere are the attacks you have chosen for battle!")
    print(chosen_moves_table)


def ready_up(current_hero, current_villain):
    hero_moves = []
    villain_moves = []

    for i in current_hero.attack:
        hero_moves.append(i.name)
    for n in current_villain.attack:
        villain_moves.append(n.name)

    ready = input(f"\nAre you ready for battle {current_hero.hero_name}?\n").lower()
    if ready == "yes":
        print("The fight begins!!")
        hero_stat_table = PrettyTable()
        hero_stat_table.field_names = ["Hero   ", "HP", "Defense", "Moves"]
        hero_stat_table.add_row([current_hero.hero_name, current_hero.hp, current_hero.hero_def,
                                 hero_moves])
        vill_stat_table = PrettyTable()
        vill_stat_table.field_names = ["Villian", "HP", "Defense", "Moves"]
        vill_stat_table.add_row([current_villain.vill_name, current_villain.hp, current_villain.vill_def,
                                 villain_moves])
        print(vill_stat_table)
        print(hero_stat_table)
        print("\n\n")
    else:
        print("Not an option you made your choice by being here, ill ask again...")
        ready_up(current_hero, current_villain)


def turn_tracker(current_hero, current_villain):
    rand_int = random.randint(0, 1)
    game_on = True
    player_turn = True

    while game_on:

        if rand_int % 2 != 0:
            player_turn = False
            print(f"\n{current_villain.vill_name}'s turn!")
            rand_int += 1
            if battle(current_hero, current_villain, player_turn) != False:
                print()
            else:
                game_on = False
        else:
            print("\nHeroes turn!")
            player_turn = True
            rand_int += 1
            if battle(current_hero, current_villain, player_turn) != False:
                print()
            else:
                game_on = False


def get_vill_attack(current_villain):
    rand_int = random.randint(0, 3)
    return current_villain.attack[rand_int - 1]


def check_health(current_hero_or_vill):
    if current_hero_or_vill.hp <= 0:
        print("GAME OVER!")
        return False
    else:
        return True


def battle(current_hero, current_villain, players_turn):

    if not players_turn:
        vill_attack = get_vill_attack(current_villain)
        vill_hit = roll(current_villain.vill_def, vill_attack)
        print(f"{current_villain.vill_name}, attacks with {vill_attack.name}!")
        print(vill_hit)
        if vill_hit == "ULTRA HIT!":
            current_hero.hp -= vill_attack.damage + 10
        if vill_hit == "CRITICAL HIT!":
            current_hero.hp -= vill_attack.damage + 5
        if vill_hit == "HIT!":
            current_hero.hp -= vill_attack.damage
        if check_health(current_hero):
            print(f"{current_hero.hero_name}'s health is now at {current_hero.hp}")
        else:
            print(f"{current_villain.vill_name} WINS!")
            return False
    else:
        #print(hero_turn_art)
        choices = []
        for i in current_hero.attack:
            choices.append({"name": i.name})
        questions = [
            {
                "type": "checkbox",
                "message": f"What attack would you like to use {current_hero.hero_name}?",
                "name": "move_list",
                "choices": choices
            }
        ]

        answer = prompt.prompt(questions)
        coded_answer = ""
        for i in answer["move_list"]:
            coded_answer = i

        moves_list = {}
        i = 0
        for move in current_hero.attack:
            moves_list[move.name] = i
            i += 1

        hero_hit = roll(current_hero.hero_def, coded_answer)
        print(f"{current_hero.hero_name}, attacks with {coded_answer}!")
        print(hero_hit)
        chosen_index = moves_list[coded_answer]
        if hero_hit == "ULTRA HIT!":
            current_villain.hp -= current_hero.attack[chosen_index].damage + 10
        if hero_hit == "CRITICAL HIT!":
            current_villain.hp -= current_hero.attack[chosen_index].damage + 5
        if hero_hit == "HIT!":
            current_villain.hp -= current_hero.attack[chosen_index].damage
        if check_health(current_villain):
            print(f"{current_villain.vill_name}'s health now at {current_villain.hp}")
            print("\n")
        else:
            print(f"{current_hero.hero_name} WINS!")
            return False


def roll(char_defense, chosen_attack):
    random_int = random.randint(0, 100)

    if random_int < char_defense:
        return "Miss!"
    elif random_int > 90:
        return "ULTRA HIT!"
    elif random_int > 80:
        return "CRITICAL HIT!"
    elif random_int > char_defense:
        return "HIT!"
