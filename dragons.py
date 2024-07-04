import random

class DragonNameGenerator:
    def __init__(self):
        self.prefixes = ["Ar", "Ba", "Drak", "Faer", "Gal", "Ign", "Ka", "Lore", "Ma", "Nym", "Pyr", "Quar", "Sar", "Thal", "Ur", "Vael", "Xar", "Yl", "Zor", "Zeph"]
        self.middles = ["ak", "ar", "dar", "dral", "gan", "lor", "mar", "nar", "orn", "ra", "ry", "sa", "tar", "thir", "tyr", "val", "vin", "wyr", "xar", "zan"]
        self.suffixes = ["ax", "ar", "dar", "dor", "dris", "gar", "gon", "ir", "ix", "lor", "mar", "nor", "rax", "ry", "th", "thar", "tor", "ur", "wyn", "zyr"]

    def generate_name(self):
        prefix = random.choice(self.prefixes)
        middle = random.choice(self.middles) if random.choice([True, False]) else ""
        suffix = random.choice(self.suffixes)
        return prefix + middle + suffix

    def generate_multiple_names(self, count=10):
        return [self.generate_name() for _ in range(count)]

# Example usage
generator = DragonNameGenerator()
for name in generator.generate_multiple_names():
    print(name)