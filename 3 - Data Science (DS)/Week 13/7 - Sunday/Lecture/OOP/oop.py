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

class Player(Character):
    def __init__(self, name, health, power):
        super().__init__(name, health, power)
    
    def input_action(self):
        action = input("Enter an action (attack/heal/quit): ")
        return action

class Enemy(Character):
    def __init__(self, name, health, power):
        super().__init__(name, health, power)

# Create instances of the player and enemy
player = Player(input("Enter your name: "), 100, 10)
enemy = Enemy("Goblin", 50, 5)

# Game loop
while True:
    # Display the current status
    print(f"\n{player.name}'s Health: {player.health}")
    print(f"{enemy.name}'s Health: {enemy.health}")
    
    # Get the player's action
    action = player.input_action()
    
    if action == "attack":
        # Player attacks the enemy
        player.attack(enemy)
        
        # Check if the enemy is defeated
        if not enemy.is_alive():
            print(f"\n{player.name} has defeated {enemy.name}!")
            break
        
        # Enemy attacks the player
        enemy.attack(player)
        
        # Check if the player is defeated
        if not player.is_alive():
            print(f"\n{player.name} has been defeated by {enemy.name}!")
            break
    
    elif action == "heal":
        # Player heals themselves
        player.heal(10)
    
    elif action == "quit":
        # Quit the game
        print(f"\n{player.name} has quit the game.")
        break
    
    else:
        print("\nInvalid action. Please choose attack, heal, or quit.")