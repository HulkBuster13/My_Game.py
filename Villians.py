class Villain:

    def __init__(self, vill_name, hp, vill_def):
        self.vill_name = vill_name
        self.hp = hp
        self.vill_def = vill_def
        self.attack = []

    def add_move(self, move):
        self.attack.append(move)


