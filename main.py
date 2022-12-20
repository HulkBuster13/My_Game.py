from Villians import Villain
from Actions import Action
from Heros import Hero
from Funtions import introduction, char_creation, choose_moves, ready_up, turn_tracker

#_+_+_+_+_+_+_+_+_+_+_+_+ TO DO _+_+_+_+_+_+_+_+_+_+_
# remove quotes around Moves in PrettyTable
# delegate winner
# disable moves when uses are out



#_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_ HEROS _+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_
# add heroes here






#_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_ VILLIANS _+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+
def add_villian_to_villain_list(villain):
    villain_list.append(villain)

villain_list = []

maganox = Villain("Magnox", 80, 50)
add_villian_to_villain_list(maganox)



heshera = Villain("Heshera", 100, 76)
add_villian_to_villain_list(heshera)




#_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+ MOVES STUFF_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+
def add_move_to_moves_list(move_object):
    moves_list.append(move_object)

moves_list = []

#GOTTA BE A BETTER WAY TO ADD THESE
punch = Action("Punch", 25, 10)
add_move_to_moves_list(punch)
kick = Action("Kick", 20, 13)
add_move_to_moves_list(kick)
slam = Action("Slam", 15, 16)
add_move_to_moves_list(slam)
smash = Action("Smash", 10, 19)
add_move_to_moves_list(smash)
clober = Action("Clober", 5, 22)
add_move_to_moves_list(clober)
spit = Action("Spit", 1, 35)
add_move_to_moves_list(spit)

maganox.add_move(kick)
maganox.add_move(punch)
maganox.add_move(slam)
maganox.add_move(smash)

#_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+ CALLER CODE +_+_+_+_+_+_+_+_+_+_+_+_+_+_+
introduction()
our_hero = Hero(char_creation(), 100, 50)
choose_moves(our_hero, moves_list)
ready_up(our_hero, maganox)
turn_tracker(our_hero, maganox)






