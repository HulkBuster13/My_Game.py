from __future__ import print_function, unicode_literals
from prettytable import PrettyTable
from PyInquirer import prompt
import hashlib
import copy
import random


ALL_TURNS = 0
actions_log = []


def sign_up():
    user_name = input("What will your Username be? ")
    password = input("What Password will you use? ")
    conf_pw = input("Re-enter Password ")

    if password == conf_pw:
        enc_pw = password.encode()
        hash1 = hashlib.md5(enc_pw).hexdigest()

        with open("credentials.txt", "w") as f:
            f.write(user_name + "\n")
            f.write(hash1)
        f.close()
        print("You have successfully registered!")

    else:
        print("Passwords do not match!")


def login():
    user_name = input("What is your Username? ")
    pwd = input("Enter password: ")

    auth = pwd.encode()
    auth_hash = hashlib.md5(auth).hexdigest()
    with open("credentials.txt", "r") as f:
        stored_username, stored_pw = f.read().split("\n")
    f.close()

    if user_name == stored_username and auth_hash == stored_pw:
        print(f"You are now logged in as {user_name}.")
    else:
        print("login Failed")
        login()


def log_sign_choice():

    questions = [
        {
            "type": "checkbox",
            "message": "Log in or Sign up?",
            "name": "choice",
            "choices": [
                {
                    'name': "Login"
                },
                {
                    'name': "Sign up"
                }
            ]
        }
    ]

    answer = prompt.prompt(questions)
    coded_answer = ""

    for i in answer["choice"]:
        coded_answer = str(i)

    if coded_answer == "Login":
        login()
    else:
        sign_up()



def char_creation():
    return input("What is your name hero?\n")


def print_attacks(hero_villain):
    moves_table = PrettyTable()
    moves_table.field_names = ["Current Attacks", "Uses", "Power"]

    for i in hero_villain.attack:
        moves_table.add_row([i.name, i.uses, i.damage])
    print(moves_table)


def check_len_attacks(hero_villain):
    return len(hero_villain.attack)


def choose_moves(our_hero, list_moves):
    moves_table = PrettyTable()
    moves_table.field_names = ["Actions", "Uses", "Power"]

    for move in list_moves:
        moves_table.add_row([move.name, move.uses, move.damage])

    print(moves_table)

    choices = []
    for i in list_moves:
        choices.append({"name": i.name})

    questions = [
        {
            "type": "checkbox",
            "message": f"What 4 moves would like to choose {our_hero.name}?",
            "name": "move_list",
            "choices": choices
        }
    ]

    answers = prompt.prompt(questions)

    for i in answers["move_list"]:
        copied_move = copy.deepcopy(i)
        our_hero.attack.append(copied_move)

    chosen_moves_table = PrettyTable()
    chosen_moves_table.field_names = ["Actions", "Uses", "Power"]

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


def print_stat_table(current_hero, current_villain):
    hero_moves = []
    villain_moves = []

    for i in current_hero.attack:
        hero_moves.append(i.name)
    for n in current_villain.attack:
        villain_moves.append(n.name)

    hero_stat_table = PrettyTable()
    hero_stat_table.field_names = ["Hero   ", "HP", "Defense", "Moves"]
    hero_stat_table.add_row([current_hero.name, current_hero.hp, current_hero.hero_def,
                             hero_moves])
    vill_stat_table = PrettyTable()
    vill_stat_table.field_names = ["Villain", "HP", "Defense", "Moves"]
    vill_stat_table.add_row([current_villain.name, current_villain.hp, current_villain.vill_def,
                             villain_moves])
    print(vill_stat_table)
    print(hero_stat_table)
    print("\n\n")


def ready_up(current_hero, current_villain):
    hero_moves = []
    villain_moves = []

    for i in current_hero.attack:
        hero_moves.append(i.name)
    for n in current_villain.attack:
        villain_moves.append(n.name)

    questions = [
        {
            "type": "checkbox",
            "message": "Are you ready for battle?",
            "name": "ready",
            "choices": [
                {
                    'name': "YES"
                },
                {
                    'name': "NO"
                }
            ]
        }
    ]

    answer = prompt.prompt(questions)
    coded_answer = ""

    for i in answer["ready"]:
        coded_answer = str(i)

    if coded_answer == "YES":
        print("The fight begins!!")
        hero_stat_table = PrettyTable()
        hero_stat_table.field_names = ["Hero", "HP", "Defense", "Moves"]
        hero_stat_table.add_row([current_hero.name, current_hero.hp, current_hero.hero_def,
                                 hero_moves])
        vill_stat_table = PrettyTable()
        vill_stat_table.field_names = ["Villain", "HP", "Defense", "Moves"]
        vill_stat_table.add_row([current_villain.name, current_villain.hp, current_villain.vill_def,
                                 villain_moves])
        print(vill_stat_table)
        print(hero_stat_table)
        print("\n\n")
        return True
    else:
        print("Not an option you made your choice by being here, ill ask again...")
        ready_up(current_hero, current_villain)


def total_turns():
    turns = 0
    turns += 1
    return turns


def turn_tracker(current_hero, current_villain):
    global ALL_TURNS
    global actions_log
    rand_int = random.randint(0, 1)
    game_on = True
    turn = 1

    while game_on:

        if rand_int % 2 != 0:
            player_turn = False
            actions_log.append({"Name": current_villain.name, "Turn": turn})
            print(f"\n{current_villain.name}'s turn!")
            rand_int += 1
            turn += 1
            ALL_TURNS += 1
            if battle(current_hero, current_villain, player_turn):
                pass
            else:
                return False
        else:
            print("\nHeroes turn!")
            player_turn = True
            actions_log.append({"Name": current_hero.name, "Turn": turn})
            rand_int += 1
            turn += 1
            ALL_TURNS += 1
            if battle(current_hero, current_villain, player_turn):
                pass
            else:
                return False



def get_vill_attack(current_villain):
    rand_int = random.randint(0, 3)
    return current_villain.attack[rand_int]


def roll(char_defense, chosen_attack, current_attacker, current_defender):
    random_int = random.randint(0, 100)
    second_random_int = random.randint(0, 100)
    hero_hit = ""
    print(f"{current_attacker.name}, attacks with {chosen_attack.name}!")

    if random_int < char_defense:
        hero_hit = "Miss!"
    elif random_int > 95 and second_random_int > 85:
        hero_hit = "OMEGA HIT!"
    elif random_int > 95:
        hero_hit = "ULTRA HIT!"
    elif random_int > 85:
        hero_hit = "CRITICAL HIT!"
    elif random_int > char_defense:
        hero_hit = "HIT!"

    actions_log.append({"Defender Info": {"Defense": char_defense, "Defender Max Hp": current_defender.max_hp}})
    actions_log.append({"Attack Info": {"Attack Used": chosen_attack.name, "Attack Damage": chosen_attack.damage,
                                        " Remaining Uses": chosen_attack.uses}})
    actions_log.append({"Roll Info": {"First Roll": random_int, "Second_Roll": second_random_int,
                                      "Hit Level": hero_hit}})
    print(hero_hit)
    before_health = current_defender.hp

    if hero_hit == "OMEGA HIT!":
        current_defender.hp -= chosen_attack.damage + 20
    if hero_hit == "ULTRA HIT!":
        current_defender.hp -= chosen_attack.damage + 10
    if hero_hit == "CRITICAL HIT!":
        current_defender.hp -= chosen_attack.damage + 5
    if hero_hit == "HIT!":
        current_defender.hp -= chosen_attack.damage

    actions_log.append({"def hp bef att": before_health, "def hp aft att": current_defender.hp})

    if check_health(current_defender):
        print(f"{current_defender.name}'s health now at {current_defender.hp}")
        return True
    else:
        print(f"{current_defender.name}, Has been vanquished!")
        print(f"{current_attacker.name} WINS!")
        return False


def check_uses(move, current_hero, current_villain, players_turn):
    if players_turn:
        if move.uses > 0:
            move.uses -= 1
            return True
        else:
            print("No more uses please choose anther move!")
            battle(current_hero, current_villain, players_turn)
    else:
        if move.uses > 0:
            move.uses -= 1
            return True
        else:
            battle(current_hero, current_villain, players_turn)


def check_health(current_hero_or_vill):
    if current_hero_or_vill.hp <= 0:
        return False
    else:
        return True


def options_screen():
    questions = [
        {
            "type": "checkbox",
            "message": "What would you like to use?",
            "name": "Options",
            "choices": [
                {
                    'name': "Attack"
                },
                {
                    'name': "Items"
                }
            ]
        }
    ]

    answer = prompt.prompt(questions)

    for i in answer["Options"]:
        coded_answer = str(i)
        return coded_answer


def get_player_attack(current_hero):

    choices = []

    for i in current_hero.attack:
        choices.append({"name": i.name})
    questions = [
        {
            "type": "checkbox",
            "message": f"What attack would you like to use {current_hero.name}?",
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
    chosen_index = moves_list[coded_answer]
    return chosen_index


def choose_new_attack(our_hero, later_moves):
    print(len(our_hero.attack))
    moves_table = PrettyTable()
    moves_table.field_names = ["New Actions", "Uses", "Power"]

    for move in later_moves:
        moves_table.add_row([move.name, move.uses, move.damage])

    print_attacks(our_hero)
    print(moves_table)

    choices = []
    for i in later_moves:
        choices.append({"name": i.name})

    questions = [
        {
            "type": "checkbox",
            "message": f"Please choose one additional move {our_hero.name}, If you already have 5 moves you will have "
                       f"to choose one to be replaced.",
            "name": "move_list",
            "choices": choices
        }
    ]

    new_answer = prompt.prompt(questions)

    for c_move in new_answer["move_list"]:
        for l_move in later_moves:
            if c_move == l_move.name and len(our_hero.attack) == 5:
                moves_table = PrettyTable()
                moves_table.field_names = ["New Actions", "Uses", "Power"]

                for move in later_moves:
                    moves_table.add_row([move.name, move.uses, move.damage])

                choices = []

                for i in our_hero.attack:
                    choices.append({"name": i.name})

                questions = [
                    {
                        "type": "checkbox",
                        "message": f"Please choose the move to be replaced {our_hero.name}.",
                        "name": "move_list",
                        "choices": choices
                    }
                ]

                replaced_answer = prompt.prompt(questions)

                for i in our_hero.attack:
                    for j in new_answer["move_list"]:
                        for k in replaced_answer["move_list"]:
                            for m in later_moves:
                                if j == m.name:
                                    j = m
                            if i.name == k:
                                our_hero.attack.remove(i)
                                our_hero.attack.append(j)
                            else:
                                pass


            if c_move == l_move.name and len(our_hero.attack) == 4:
                our_hero.attack.append(l_move)



def choose_item(current_hero):
    choices = []

    for i in current_hero.items:
        choices.append({"name": i.name})

    questions = [
        {
            "type": "checkbox",
            "message": f"What item would you like to use {current_hero.name}?",
            "name": "Items",
            "choices": choices
        }
    ]

    answer = prompt.prompt(questions)
    coded_answer = ""

    for i in answer["Items"]:
        coded_answer = i

    item_list = {}
    i = 0

    for item in current_hero.items:
        item_list[item.name] = i
        i += 1

    chosen_index = item_list[coded_answer]
    return chosen_index


def use_potion(current_hero_vill, item):
    if current_hero_vill.hp == current_hero_vill.max_hp:
        print("Already at full health!")
    else:
        if current_hero_vill.hp < current_hero_vill.max_hp:
            current_hero_vill.hp += item.heal_factor
            heal_amount = item.heal_factor
            if current_hero_vill.hp > current_hero_vill.max_hp:
                subtractor = current_hero_vill.hp - current_hero_vill.max_hp
                heal_amount = heal_amount - subtractor
                current_hero_vill.hp = current_hero_vill.max_hp
            print(f"{current_hero_vill.name} heals {heal_amount}.")


def add_health(current_hero_vill, action):
    before_health = current_hero_vill.hp
    if current_hero_vill.hp == current_hero_vill.max_hp:
        print("Already at full health!")
    else:
        if current_hero_vill.hp < current_hero_vill.max_hp:
            current_hero_vill.hp += action.heal_factor
            heal_amount = action.heal_factor
            if current_hero_vill.hp > current_hero_vill.max_hp:
                subtractor = current_hero_vill.hp - current_hero_vill.max_hp
                heal_amount = heal_amount - subtractor
                current_hero_vill.hp = current_hero_vill.max_hp
            print(f"{current_hero_vill.name} heals {heal_amount}.")
            actions_log.append({"Hp before heal": before_health, "hp after heal": current_hero_vill.hp,
                                "Health gained": heal_amount})


def health_check(current_hero, current_villain, players_turn, move_cat, hero_attack):
    villain_defense = current_villain.vill_def

    if move_cat == "Healing" and current_hero.hp == current_hero.max_hp:
        print("You're health is full, ATTACK!!")
        chosen_index = get_player_attack(current_hero)
        new_answer = current_hero.attack[chosen_index]
        if check_uses(new_answer, current_hero, current_villain, players_turn):
            roll(villain_defense, new_answer, current_hero, current_villain)
    else:
        add_health(current_hero, hero_attack)
        print(f"{current_hero.name}'s health is now at {current_hero.hp}")



def battle(current_hero, current_villain, players_turn):

    if not players_turn:
        vill_attack = get_vill_attack(current_villain)
        hero_defense = current_hero.hero_def

        while vill_attack.category == "Healing" and current_villain.hp == current_villain.max_hp:
            vill_attack = get_vill_attack(current_villain)

        if check_uses(vill_attack, current_hero, current_villain, players_turn):
            if vill_attack.category == "Healing":
                add_health(current_villain, vill_attack)
                print(f"{current_villain.name}'s hp now at {current_villain.hp}")
            else:
                roll(hero_defense, vill_attack, current_villain, current_hero)
        if check_health(current_hero):
            return True
        else:
            return False
    else:
        chosen_option = options_screen()
        villain_defense = current_villain.vill_def

        if chosen_option == "Attack":
            chosen_index = get_player_attack(current_hero)
            hero_attack = current_hero.attack[chosen_index]
            move_category = current_hero.attack[chosen_index].category
            # move_type = current_hero.attack[chosen_index].type <<< for when you get types set up in actions

            if check_uses(hero_attack, current_hero, current_villain, players_turn):
                if move_category == "Healing":
                    health_check(current_hero, current_villain, players_turn, move_category, hero_attack)
                else:
                    roll(villain_defense, hero_attack, current_hero, current_villain)

        if chosen_option == "Items":
            chosen_index = choose_item(current_hero)
            item_index = current_hero.items[chosen_index]
            item_type = current_hero.items[chosen_index].category

            if item_type == "Health Potion" and current_hero.hp == current_hero.max_hp:
                print("You're health is full, ATTACK!!")
                chosen_index = get_player_attack(current_hero)
                new_index = current_hero.attack[chosen_index]
                if check_uses(new_index, current_hero, current_villain, players_turn):
                    roll(current_hero.hero_def, new_index, current_hero, current_villain)
            else:
                if check_uses(item_index, current_hero, current_villain, players_turn):
                    add_health(current_hero, item_index)
                    print(f"{current_hero.name}'s health is now at {current_hero.hp}")
        if check_health(current_villain):
            return True
        else:
            return False

