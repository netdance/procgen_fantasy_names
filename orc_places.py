import random

class OrcishPlaceNameGenerator:
    def __init__(self):
        self.prefixes = ["Ghor", "Grak", "Krog", "Larg", "Mog", "Nar", "Ork", "Rug", "Thok", "Ugr", "Vor", "Zog", "Blarg", "Drag", "Garg", "Hrak", "Krag", "Lurk", "Snag", "Thr"]
        self.middles = ["ak", "ar", "dor", "gar", "gor", "krak", "lag", "mak", "nak", "ork", "rag", "rok", "thak", "urg", "varg", "zag", "zurk", "gar", "mor", "zar"]
        self.suffixes = ["brawl", "chasm", "den", "fang", "fort", "hold", "keep", "lair", "mire", "pit", "ravine", "rock", "spire", "stronghold", "throk", "tower", "valley", "warren", "wasteland", "zerk"]

    def generate_place_name(self):
        prefix = random.choice(self.prefixes)
        middle = random.choice(self.middles) if random.choice([True, False]) else ""
        suffix = random.choice(self.suffixes)
        return prefix + middle + suffix

    def generate_multiple_names(self, count=10):
        return [self.generate_place_name() for _ in range(count)]

# Example usage
generator = OrcishPlaceNameGenerator()
for name in generator.generate_multiple_names():
    print(name)