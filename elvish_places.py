import random

class ElvishPlaceNameGenerator:
    def __init__(self):
        self.prefixes = ["Ae", "Al", "Ar", "Bel", "Cael", "Dael", "El", "Fael", "Gal", "Il", "Lae", "Loth", "Mir", "Nael", "Quel", "Sael", "Thael", "Vael", "Yl", "Zae"]
        self.middles = ["ad", "aer", "am", "ar", "eir", "en", "il", "im", "ir", "is", "lan", "lor", "mir", "nar", "nel", "ra", "rel", "rin", "sa", "thal"]
        self.suffixes = ["adell", "dale", "dorn", "dril", "endor", "far", "land", "londe", "lorien", "mar", "men", "mith", "nor", "reth", "riel", "thas", "thien", "tir", "vahl", "wyn"]

    def generate_place_name(self):
        prefix = random.choice(self.prefixes)
        middle = random.choice(self.middles) if random.choice([True, False]) else ""
        suffix = random.choice(self.suffixes)
        return prefix + middle + suffix

    def generate_multiple_names(self, count=10):
        return [self.generate_place_name() for _ in range(count)]

# Example usage
generator = ElvishPlaceNameGenerator()
for name in generator.generate_multiple_names():
    print(name)