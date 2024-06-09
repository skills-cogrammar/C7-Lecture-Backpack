# Define the player's attributes
player_name = ""
player_health = 100
player_power = 10

# Define the enemy's attributes
enemy_name = "Goblin"
enemy_health = 50
enemy_power = 5

# Get the player's name
player_name = input("Enter your name: ")

# Game loop
while True:
    # Display the current status
    print(f"\n{player_name}'s Health: {player_health}")
    print(f"{enemy_name}'s Health: {enemy_health}")
    
    # Get the player's action
    action = input("Enter an action (attack/heal/quit): ")
    
    if action == "attack":
        # Player attacks the enemy
        enemy_health -= player_power
        print(f"\n{player_name} attacks {enemy_name} for {player_power} damage!")
        
        # Check if the enemy is defeated
        if enemy_health <= 0:
            print(f"\n{player_name} has defeated {enemy_name}!")
            break
        
        # Enemy attacks the player
        player_health -= enemy_power
        print(f"{enemy_name} attacks {player_name} for {enemy_power} damage!")
        
        # Check if the player is defeated
        if player_health <= 0:
            print(f"\n{player_name} has been defeated by {enemy_name}!")
            break
    
    elif action == "heal":
        # Player heals themselves
        heal_amount = 10
        player_health += heal_amount
        print(f"\n{player_name} heals for {heal_amount} health!")
    
    elif action == "quit":
        # Quit the game
        print(f"\n{player_name} has quit the game.")
        break
    
    else:
        print("\nInvalid action. Please choose attack, heal, or quit.")