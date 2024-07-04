import random

class GiantPlaceNameGenerator:
    def __init__(self):
        self.prefixes = ["Brag", "Brom", "Drun", "Grom", "Hro", "Jor", "Kar", "Krag", "Lok", "Mar", "Mor", "Nor", "Orm", "Ragn", "Stor", "Thar", "Thor", "Urg", "Var", "Zor"]
        self.middles = ["gan", "gro", "kar", "lor", "mar", "nor", "rak", "ron", "tar", "thok", "thun", "tor", "var", "vor", "zor", "zan", "zgar", "zir", "drak", "grim"]
        self.suffixes = ["berg", "crag", "dale", "fell", "forge", "gar", "heim", "hold", "keep", "land", "peak", "rock", "spire", "stead", "thok", "tor", "vale", "wall", "wyrm", "zorn"]

    def generate_place_name(self):
        prefix = random.choice(self.prefixes)
        middle = random.choice(self.middles) if random.choice([True, False]) else ""
        suffix = random.choice(self.suffixes)
        return prefix + middle + suffix

    def generate_multiple_names(self, count=10):
        return [self.generate_place_name() for _ in range(count)]

# Example usage
generator = GiantPlaceNameGenerator()
for name in generator.generate_multiple_names():
    print(name)