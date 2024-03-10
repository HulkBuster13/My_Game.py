import copy


class Villain:

    def __init__(self, name, hp, max_hp, vill_def):
        self.name = name
        self.hp = hp
        self.max_hp = max_hp
        self.vill_def = vill_def
        self.level = "add level object here (create level class)"
        self.attack = []
        self.items = []

    def add_move(self, move):
        self.attack.append(move)

    def add_potion(self, item):
        copied_item = copy.deepcopy(item)
        self.items.append(copied_item)


class FireWarlockVillain(Villain):

    def __init__(self, name, hp, max_hp, vill_def, fire_resist, fire_boost):
        super().__init__(name, hp, max_hp, vill_def)
        self.fire_resist = fire_resist
        self.fire_boost = fire_boost
        self.type = "Fire"
        self.weakness = "Earth"


class TechromancerVillain(Villain):

    def __init__(self, name, hp, max_hp, vill_def, tech_resist, tech_boost):
        super().__init__(name, hp, max_hp, vill_def)
        self.fire_resist = tech_resist
        self.fire_boost = tech_boost
        self.type = "Tech"
        self.weakness = "Water"


class WaterEnchanterVillain(Villain):

    def __init__(self, name, hp, max_hp, vill_def, water_resist, water_boost):
        super().__init__(name, hp, max_hp, vill_def)
        self.fire_resist = water_resist
        self.fire_boost = water_boost
        self.type = "Water"
        self.weakness = "Shaman"


class EarthOperatorVillain(Villain):

    def __init__(self, name, hp, max_hp, vill_def, earth_resist, earth_boost):
        super().__init__(name, hp, max_hp, vill_def)
        self.fire_resist = earth_resist
        self.fire_boost = earth_boost
        self.type = "Earth"
        self.weakness = "Telepath"


class TelepathVillain(Villain):

    def __init__(self, name, hp, max_hp, vill_def, fire_resist, fire_boost):
        super().__init__(name, hp, max_hp, vill_def)
        self.fire_resist = fire_resist
        self.fire_boost = fire_boost
        self.type = "Telepath"
        self.weakness = "Tech"


class BioVillain(Villain):

    def __init__(self, name, hp, max_hp, vill_def, bio_resist, bio_boost):
        super().__init__(name, hp, max_hp, vill_def)
        self.bio_resist = bio_resist
        self.bio_boost = bio_boost
        self.type = "Bio"
        self.weakness = "Fire"


class ShamanVillain(Villain):

    def __init__(self, name, hp, max_hp, vill_def, damage_resist, heal_increase, attack_decrease):
        super().__init__(name, hp, max_hp, vill_def)
        self.damage_resist = damage_resist
        self.heal_increase = heal_increase
        self.attack_decrease = attack_decrease
        self.type = "Shaman"



