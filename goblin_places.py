import random

class GoblinPlaceNameGenerator:
    def __init__(self):
        self.prefixes = ["Blik", "Chak", "Crik", "Drit", "Fik", "Gak", "Grik", "Krak", "Nak", "Prik", "Rak", "Snak", "Tik", "Vrik", "Zik", "Zok", "Yik", "Jik", "Xak", "Blat"]
        self.middles = ["ak", "ik", "ek", "ok", "uk", "an", "en", "in", "on", "un", "ir", "ar", "er", "or", "ur", "iz", "az", "ez", "oz", "uz"]
        self.suffixes = ["berg", "bite", "bog", "burrow", "cave", "den", "gnarl", "hall", "hollow", "keep", "lair", "mire", "nest", "pit", "pox", "scarp", "shard", "snarl", "spire", "warren"]

    def generate_place_name(self):
        prefix = random.choice(self.prefixes)
        middle = random.choice(self.middles) if random.choice([True, False]) else ""
        suffix = random.choice(self.suffixes)
        return prefix + middle + suffix

    def generate_multiple_names(self, count=10):
        return [self.generate_place_name() for _ in range(count)]

# Example usage
generator = GoblinPlaceNameGenerator()
for name in generator.generate_multiple_names():
    print(name)