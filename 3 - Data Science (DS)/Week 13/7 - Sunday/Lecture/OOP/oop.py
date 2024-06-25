from Characters.player import Player
from Characters.enemy import Enemy

# Create instances of the player and enemy
player = Player(input("Enter your name: "), 100, 10)
enemy = Enemy("Goblin", 50, 5)
enemy_2 = Enemy("Orc", 100, 10)

# Game loop
while True:
    # Display the current status
    print(f"\n{player.name}'s Health: {player.health}")
    print(f"{enemy.name}'s Health: {enemy.health}")
    print(f"{enemy_2.name}'s Health: {enemy_2.health}")
    
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