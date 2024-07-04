import random

class WeaponNameGenerator:
    def __init__(self):
        self.prefixes = ["Ash", "Blood", "Dark", "Doom", "Dragon", "Dwarf", "Elf", "Fire", "Flame", "Frost", "Giant", "Gold", "Iron", "Light", "Moon", "Night", "Orc", "Shadow", "Silver", "Storm"]
        self.middles = ["bane", "breaker", "bringer", "cleaver", "crusher", "edge", "flame", "frost", "guard", "hammer", "heart", "keeper", "master", "rage", "reaper", "shard", "singer", "smite", "soul", "strike"]
        self.suffixes = ["Axe", "Blade", "Bow", "Edge", "Fang", "Flail", "Hammer", "Lance", "Mace", "Scythe", "Shield", "Spear", "Staff", "Sword", "Talon", "Whip", "Claw", "Dagger", "Sabre", "Maul"]

    def generate_weapon_name(self):
        prefix = random.choice(self.prefixes)
        middle = random.choice(self.middles)
        suffix = random.choice(self.suffixes)
        return f"{prefix}{middle} {suffix}"

    def generate_multiple_names(self, count=10):
        return [self.generate_weapon_name() for _ in range(count)]

# Example usage
generator = WeaponNameGenerator()
for name in generator.generate_multiple_names():
    print(name)