from Characters.character import Character

class Enemy(Character):
    def __init__(self, name, health, power):
        super().__init__(name, health, power)

    def cry_out_for_help(self):
        if self.health == 0:
            print("Oh no!!! I'm defeated.")