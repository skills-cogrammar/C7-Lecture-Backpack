class Poke:
    all_poke = []

    def __init__(self, name, poke_type):
        self.name = name
        self.poke_type = poke_type
        self.moves = []

    def add_move(self, poke_move):
        self.moves.append(poke_move)

    @classmethod
    def view_all(cls):
        print("Current Pokemon:")
        for poke in cls.all_poke:
            print(poke.name)

    @staticmethod
    def calc_damage(att, deff):
        return att - deff


# Creating instances of Pokemon
pikachu = Poke("Pikachu", "Electric")
slowpoke = Poke("Slowpoke", "Psychic")
charizard = Poke("Charizard", "Fire")

# Adding moves to Pokemon
pikachu.add_move("thunderbolt!")
slowpoke.add_move("tax evasion!")
charizard.add_move("sharingan!")


# Adding Pokemon to the list of all Pokemon
Poke.all_poke.append(pikachu)
Poke.all_poke.append(slowpoke)
Poke.all_poke.append(charizard)


print(pikachu.moves)
print(slowpoke.moves)
print(charizard.moves)

# Displaying all Pokemon
Poke.view_all()

# Calculating damage using static method
damage = Poke.calc_damage(40, 10)
print(f"Damage: {damage}")
