import random

class OrcNameGenerator:
    def __init__(self):
        self.prefixes = ["Gha", "Gru", "Kra", "Lag", "Mog", "Nar", "Or", "Rug", "Thok", "Ugr", "Vor", "Zag", "Blar", "Dur", "Gal", "Har", "Kar", "Lur", "Ruk", "Thr"]
        self.middles = ["agh", "ark", "dor", "gar", "gor", "khar", "lag", "mak", "nak", "ork", "rag", "rok", "thak", "urg", "varg", "zag", "zurk", "gar", "mor", "zar"]
        self.suffixes = ["ak", "ar", "ash", "ek", "gor", "ir", "kor", "lak", "mak", "nar", "ork", "rak", "tar", "uk", "ur", "ush", "var", "zor", "zur", "thok"]

    def generate_name(self):
        prefix = random.choice(self.prefixes)
        middle = random.choice(self.middles) if random.choice([True, False]) else ""
        suffix = random.choice(self.suffixes)
        return prefix + middle + suffix

    def generate_multiple_names(self, count=10):
        return [self.generate_name() for _ in range(count)]

# Example usage
generator = OrcNameGenerator()
for name in generator.generate_multiple_names():
    print(name)