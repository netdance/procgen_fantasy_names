import random

class DragonPlaceNameGenerator:
    def __init__(self):
        self.prefixes = ["Ar", "Dra", "Faer", "Gal", "Ign", "Ka", "Lor", "Ma", "Nym", "Pyr", "Quar", "Sar", "Thal", "Ur", "Vael", "Xar", "Yl", "Zor", "Zeph", "Saph"]
        self.middles = ["ak", "ar", "dor", "dral", "gan", "lor", "mar", "nar", "orn", "ra", "ry", "sa", "tar", "thir", "tyr", "val", "vin", "wyr", "xar", "zan"]
        self.suffixes = ["an", "ar", "dor", "dril", "endor", "far", "londe", "mar", "men", "nor", "reth", "riel", "thas", "thien", "tir", "vahl", "wyn", "ax", "zyr", "mount"]

    def generate_place_name(self):
        prefix = random.choice(self.prefixes)
        middle = random.choice(self.middles) if random.choice([True, False]) else ""
        suffix = random.choice(self.suffixes)
        return prefix + middle + suffix

    def generate_multiple_names(self, count=10):
        return [self.generate_place_name() for _ in range(count)]

# Example usage
generator = DragonPlaceNameGenerator()
for name in generator.generate_multiple_names():
    print(name)