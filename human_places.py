import random

class KingdomNameGenerator:
    def __init__(self):
        self.prefixes = ["Al", "Ar", "Bris", "Cal", "Dar", "Eld", "Fen", "Gal", "Hal", "Is", "Jan", "Kal", "Lan", "Mar", "Nor", "Ol", "Pen", "Quin", "Ran", "Tal"]
        self.middles = ["bor", "dar", "el", "en", "eth", "gar", "lor", "mar", "nor", "rin", "tar", "thal", "tin", "tor", "val", "vin", "wes", "wyn", "zor", "zan"]
        self.suffixes = ["dale", "don", "dor", "fell", "ford", "gate", "hold", "keep", "land", "march", "mere", "port", "reach", "rest", "shire", "stead", "vale", "watch", "wick", "worth"]

    def generate_kingdom_name(self):
        prefix = random.choice(self.prefixes)
        middle = random.choice(self.middles) if random.choice([True, False]) else ""
        suffix = random.choice(self.suffixes)
        return prefix + middle + suffix

    def generate_multiple_names(self, count=10):
        return [self.generate_kingdom_name() for _ in range(count)]

# Example usage
generator = KingdomNameGenerator()
for name in generator.generate_multiple_names():
    print(name)