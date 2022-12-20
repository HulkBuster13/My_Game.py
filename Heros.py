class Hero:

    def __init__(self, hero_name, hp, hero_def):
        self.hero_name = hero_name
        self.hp = hp
        self.hero_def = hero_def
        self.attack = []

    def add_move(self, move):
        self.attack.append(move)

hero_turn_art = " _   _  _____ ______  _____  _____   _____  _   _ ______  _   _ " \
                "| | | ||  ___|| ___ \|  _  |/  ___| |_   _|| | | || ___ \| \ | |" \
                "| |_| || |__  | |_/ /| | | |\ `--.    | |  | | | || |_/ /|  \| |" \
                "|  _  ||  __| |    / | | | | `--. \   | |  | | | ||    / | . ` |" \
                "| | | || |___ | |\ \ \ \_/ //\__/ /   | |  | |_| || |\ \ | |\  |" \
                "\_| |_/\____/ \_| \_| \___/ \____/    \_/   \___/ \_| \_|\_| \_/"

