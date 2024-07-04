import random

class DwarfNameGenerator:
    def __init__(self):
        self.prefixes = ["Bal", "Bar", "Bor", "Dag", "Dur", "Fal", "Gar", "Gim", "Gor", "Kil", "Mor", "Nor", "Orin", "Thal", "Thor", "Ulf", "Ulr", "Var", "Varr", "Zar"]
        self.middles = ["aim", "ar", "dor", "dur", "gim", "gon", "grim", "gun", "ir", "kor", "or", "rin", "rum", "tarn", "thor", "ur", "var", "zin", "zon", "zun"]
        self.suffixes = ["ak", "an", "ar", "bar", "dak", "din", "dor", "gar", "gim", "in", "kor", "lam", "lor", "mar", "nor", "orn", "rin", "rum", "thar", "ur"]

    def generate_name(self):
        prefix = random.choice(self.prefixes)
        middle = random.choice(self.middles) if random.choice([True, False]) else ""
        suffix = random.choice(self.suffixes)
        return prefix + middle + suffix

    def generate_multiple_names(self, count=10):
        return [self.generate_name() for _ in range(count)]

# Example usage
generator = DwarfNameGenerator()
for name in generator.generate_multiple_names():
    print(name)