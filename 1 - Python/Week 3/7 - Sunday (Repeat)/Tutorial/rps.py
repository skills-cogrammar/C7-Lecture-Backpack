import random

def get_user_choice():
    while True:
        try:
            user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
            if user_choice not in ['rock', 'paper', 'scissors']:
                raise ValueError("Invalid choice! Please enter 'rock', 'paper', or 'scissors'.")
            return user_choice
        except ValueError as ve:
            print(ve)

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    print("Let's play Rock, Paper, Scissors!")
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    print("You chose:", user_choice)
    print("Computer chose:", computer_choice)
    print(determine_winner(user_choice, computer_choice))

# Play the game
play_game()


