import random

class GoblinNameGenerator:
    def __init__(self):
        self.prefixes = ["Bik", "Blit", "Chak", "Crik", "Drit", "Fik", "Gak", "Grib", "Krik", "Nak", "Prik", "Rak", "Snit", "Tik", "Vrik", "Zik", "Zok", "Yik", "Jik", "Xak"]
        self.middles = ["ik", "ak", "ek", "ok", "uk", "in", "an", "en", "on", "un", "ir", "ar", "er", "or", "ur", "iz", "az", "ez", "oz", "uz"]
        self.suffixes = ["bit", "dik", "gik", "kip", "lik", "nik", "pik", "rik", "sik", "tik", "vik", "zik", "zab", "zib", "zot", "zop", "zut", "zim"]

    def generate_name(self):
        prefix = random.choice(self.prefixes)
        middle = random.choice(self.middles) if random.choice([True, False]) else ""
        suffix = random.choice(self.suffixes)
        return prefix + middle + suffix

    def generate_multiple_names(self, count=10):
        return [self.generate_name() for _ in range(count)]

# Example usage
generator = GoblinNameGenerator()
for name in generator.generate_multiple_names():
    print(name)