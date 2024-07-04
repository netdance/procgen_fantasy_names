import random

class DwarvishPlaceNameGenerator:
    def __init__(self):
        self.prefixes = ["Bar", "Bal", "Dain", "Dur", "Far", "Gar", "Gim", "Gor", "Kaz", "Kil", "Mor", "Nor", "Orin", "Thal", "Thor", "Ulf", "Ulr", "Var", "Varr", "Zar"]
        self.middles = ["am", "bar", "dal", "dor", "gar", "gim", "gon", "ir", "khar", "lor", "mak", "nar", "rin", "rok", "rum", "thal", "tor", "ul", "var", "zar"]
        self.suffixes = ["bar", "bek", "dal", "dar", "dur", "gar", "gim", "gor", "in", "kar", "lom", "mor", "nad", "nor", "rak", "rim", "tor", "ur", "zin", "zor"]

    def generate_place_name(self):
        prefix = random.choice(self.prefixes)
        middle = random.choice(self.middles) if random.choice([True, False]) else ""
        suffix = random.choice(self.suffixes)
        return prefix + middle + suffix

    def generate_multiple_names(self, count=10):
        return [self.generate_place_name() for _ in range(count)]

# Example usage
generator = DwarvishPlaceNameGenerator()
for name in generator.generate_multiple_names():
    print(name)