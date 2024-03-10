class Action:

    def __init__(self, name, uses, max_uses, damage, category):
        self.name = name
        self.uses = uses
        self.max_uses = max_uses
        self.damage = damage
        self.category = category
        self.level = 0 # your actions should level up after using them a certain number of times


class FireAction(Action):

    def __init__(self, name, uses, max_uses, damage, category):
        super().__init__(name, uses, max_uses, damage, category)
        self.type = "Fire"


class TechAction(Action):

    def __init__(self, name, uses, max_uses, damage, category):
        super().__init__(name, uses, max_uses, damage, category)
        self.type = "Tech"


class WaterAction(Action):

    def __init__(self, name, uses, max_uses, damage, category):
        super().__init__(name, uses, max_uses, damage, category)
        self.type = "Water"


class EarthAction(Action):

    def __init__(self, name, uses, max_uses, damage, category):
        super().__init__(name, uses, max_uses, damage, category)
        self.type = "Earth"


class TelepathAction(Action):

    def __init__(self, name, uses, max_uses, damage, category):
        super().__init__(name, uses, max_uses, damage, category)
        self.type = "Telepath"


class ProtectorAction(Action):

    def __init__(self, name, uses, max_uses, damage, category, heal_factor):
        super().__init__(name, uses, max_uses, damage, category)
        self.heal_factor = heal_factor
        self.type = "Protector"

