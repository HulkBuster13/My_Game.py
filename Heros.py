class Hero:

    def __init__(self, hero_name, hp, hero_def):
        self.hero_name = hero_name
        self.hp = hp
        self.hero_def = hero_def
        self.attack = []

    def add_move(self, move):
        self.attack.append(move)