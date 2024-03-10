import copy


class Hero:

    def __init__(self, name, hp, max_hp, hero_def):
        self.name = name
        self.hp = hp
        self.max_hp = max_hp
        self.hero_def = hero_def
        self.level = "add level object here(create level class"
        self.attack = []
        self.items = []

    def add_move(self, move):
        self.attack.append(move)

    def add_potion(self, item):
        copied_item = copy.deepcopy(item)
        self.items.append(copied_item)


class FireWarlockHero(Hero):

    def __init__(self, name, hp, max_hp, hero_def, fire_resist, fire_boost):
        super().__init__(name, hp, max_hp, hero_def)
        self.fire_resist = fire_resist
        self.fire_boost = fire_boost
        self.type = "Fire"
        self.weakness = "Earth"


class TechromancerHero(Hero):

    def __init__(self, name, hp, max_hp, hero_def, tech_resist, tech_boost):
        super().__init__(name, hp, max_hp, hero_def)
        self.tech_resist = tech_resist
        self.tech_boost = tech_boost
        self.type = "Tech"
        self.weakness = "Water"


class WaterEnchanterHero(Hero):

    def __init__(self, name, hp, max_hp, hero_def, water_resist, water_boost):
        super().__init__(name, hp, max_hp, hero_def)
        self.water_resist = water_resist
        self.water_boost = water_boost
        self.type = "Water"
        self.weakness = "Bio"


class EarthOperatorHero(Hero):

    def __init__(self, name, hp, max_hp, hero_def, earth_resist, earth_boost):
        super().__init__(name, hp, max_hp, hero_def)
        self.earth_resist = earth_resist
        self.earth_boost = earth_boost
        self.type = "Earth"
        self.weakness = "Telepath"


class TelepathHero(Hero):

    def __init__(self, name, hp, max_hp, hero_def, telepath_resist, telepath_boost):
        super().__init__(name, hp, max_hp, hero_def)
        self.telepath_resist = telepath_resist
        self.telepath_boost = telepath_boost
        self.type = "Telepath"
        self.weakness = "Tech"


class BioHero(Hero):

    def __init__(self, name, hp, max_hp, hero_def, bio_resist, bio_boost):
        super().__init__(name, hp, max_hp, hero_def)
        self.bio_resist = bio_resist
        self.bio_boost = bio_boost
        self.type = "Bio"
        self.weakness = "Fire"


class ShamanHero(Hero):

    def __init__(self, name, hp, max_hp, hero_def, damage_reduction, heal_boost, weakness):
        super().__init__(name, hp, max_hp, hero_def)
        self.damage_reduction = damage_reduction
        self.heal_boost = heal_boost
        self.weakness = weakness

