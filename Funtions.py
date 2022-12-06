import random
from prettytable import PrettyTable



def introduction():
    print("Welcome to The Tower...Good luck getting to the top...Youre going to need it...")


def char_creation():
    return input("What is your name hero?\n")


def choose_moves(our_hero, list_moves):
    print(f"Hello {our_hero.hero_name}, Choose 4 Moves from the list below:")
    moves_table = PrettyTable()
    moves_table.field_names = ["Name", "Uses", "Damage"]
    moves_table.add_row(["Punch", 25, 10])
    moves_table.add_row(["Kick", 20, 13])
    moves_table.add_row(["Slam", 15, 16])
    moves_table.add_row(["Smash", 10, 19])
    moves_table.add_row(["Clober", 5, 22])
    print(moves_table)
    chosen = input("What 4 moves will you choose? Please separate choices with a comma and a space.\n")
    chosen_moves = chosen.split(", ")

    for c_move in chosen_moves:
        for l_move in list_moves:
            if l_move.name == c_move:
                our_hero.attack.append(l_move)

    chosen_moves_table = PrettyTable()
    chosen_moves_table.field_names = ["Name", "Uses", "Damage"]
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
            print(f"{current_villain.vill_name}'s turn!")
            rand_int += 1
            battle(current_hero, current_villain, player_turn)

        else:
            print("Your turn!")
            player_turn = True
            rand_int += 1
            battle(current_hero, current_villain, player_turn)


def battle(current_hero, current_villain, players_turn):
    rand_int = random.randint(0, len(current_villain.attack))

    if not players_turn:
        vill_hit = roll(current_villain.vill_def, current_villain.attack[rand_int - 1])
        print("Villain turn Working!")
        print(vill_hit)
        if roll != "Miss!":
            current_hero.hp -= current_villain.attack[rand_int -1].damage
            print(f"curent hero hp = {current_hero.hp}")
    else:
        chosen_attack = input(f"What attack would you like to use? ({current_hero.attack[0].name},"
                              f" {current_hero.attack[1].name}, {current_hero.attack[2].name}, "
                              f"{current_hero.attack[3].name})\n")
        moves_list = {}
        i = 0
        for move in current_hero.attack:
            moves_list[move.name] = i
            i += 1
        print(moves_list)

        hero_hit = roll(current_hero.hero_def, chosen_attack)
        print("Hero turn working")
        print(hero_hit)
        if roll != "Miss!":
            chosen_index = moves_list[chosen_attack]
            print(chosen_index)
            current_villain.hp -= current_hero.attack[chosen_index].damage
            print(f"current villian hp = {current_villain.hp}")


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