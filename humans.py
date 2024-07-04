import random

class FantasyHumanNameGenerator:
    def __init__(self):
        self.prefixes = ["Al", "Ar", "Ben", "Cal", "Dan", "El", "Fen", "Gal", "Hal", "Is", "Jan", "Kal", "Lan", "Mal", "Nor", "Ol", "Pen", "Quin", "Ran", "Tal"]
        self.middles = ["an", "ar", "el", "en", "ir", "is", "or", "os", "ra", "rin", "ta", "ten", "val", "vin", "lor", "las", "dar", "lan", "lin", "tor"]
        self.suffixes = ["an", "ar", "el", "en", "ian", "is", "or", "us", "as", "ar", "on", "al", "os", "ur", "ar", "in", "al", "ar", "en", "is"]

    def generate_name(self):
        prefix = random.choice(self.prefixes)
        middle = random.choice(self.middles) if random.choice([True, False]) else ""
        suffix = random.choice(self.suffixes)
        return prefix + middle + suffix

    def generate_multiple_names(self, count=10):
        return [self.generate_name() for _ in range(count)]

# Example usage
generator = FantasyHumanNameGenerator()
for name in generator.generate_multiple_names():
    print(name)