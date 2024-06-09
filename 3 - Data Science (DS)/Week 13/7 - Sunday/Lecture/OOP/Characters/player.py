from Characters.character import Character

class Player(Character):
    def __init__(self, name, health, power):
        super().__init__(name, health, power)
    
    def input_action(self):
        action = input("Enter an action (attack/heal/quit): ")
        return action