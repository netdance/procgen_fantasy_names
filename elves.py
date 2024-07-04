import random

class ElvenNameGenerator:
    def __init__(self):
        self.prefixes = ["Ae", "Al", "Ar", "Ba", "Be", "Ca", "Da", "El", "Fa", "Ga", "Ha", "Il", "La", "Ma", "Na", "Ra", "Sa", "Ta", "Va", "Ze"]
        self.middles = ["da", "ra", "la", "mi", "ne", "ri", "sa", "tha", "vi", "we", "ya", "di", "lo", "ma", "na", "re", "si", "ta", "va", "zi"]
        self.suffixes = ["el", "en", "eth", "il", "im", "in", "ir", "is", "ith", "la", "na", "nel", "ra", "ral", "ren", "ria", "riel", "ril", "ro", "sin"]

    def generate_name(self):
        prefix = random.choice(self.prefixes)
        middle = random.choice(self.middles) if random.choice([True, False]) else ""
        suffix = random.choice(self.suffixes)
        return prefix + middle + suffix

    def generate_multiple_names(self, count=10):
        return [self.generate_name() for _ in range(count)]

# Example usage
generator = ElvenNameGenerator()
for name in generator.generate_multiple_names():
    print(name)