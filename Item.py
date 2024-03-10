class Item:

    def __init__(self, name, uses, category):
        self.name = name
        self.uses = uses
        self.category = category


class HealthItem(Item):

    def __init__(self, name, uses, category, heal_factor):
        super().__init__(name, uses, category)
        self.heal_factor = heal_factor


class DefensiveItem(Item):

    def __init__(self, name, uses, category, defensive_factor):
        super().__init__(name, uses, category)
        self.defensive_factor = defensive_factor


class TurnCreditBoostItem(Item):

    def __init__(self, name, uses, category, defensive_factor):
        super().__init__(name, uses, category)
        self.defensive_factor = defensive_factor


class ReviveItem(Item):

    def __init__(self, name, uses, category, revive, heal_factor):
        super().__init__(name, uses, category)
        self.revive = revive
        self.heal_factor = heal_factor
