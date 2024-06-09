class Character:
    def __init__(self, name, health, power):
        self.name = name
        self.health = health
        self.power = power
    
    def is_alive(self):
        return self.health > 0
    
    def attack(self, other):
        other.health -= self.power
        print(f"\n{self.name} attacks {other.name} for {self.power} damage!")
    
    def heal(self, amount):
        self.health += amount
        print(f"\n{self.name} heals for {amount} health!")