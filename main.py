import random

choices = ["Rock","Paper","Scissors"]

player_choice = input("Enter your choice: Rock, Paper, Scissor: " ).capitalize()

while player_choice not in choices:

    print("Please enter a valid choice!")
    player_choice = input("Enter your choice: Rock, Paper, Scissors: ").capitalize()

computer_choice = random.choice(choices)

def determine_winner(player_choice,computer_choice):
    if player_choice == computer_choice:
        return "It's a tie"
    elif player_choice == "Rock" and computer_choice == "Scissors" or player_choice == "Paper" and computer_choice == "Rock" or player_choice == "Scissors" and computer_choice == "Paper":
        return "You Win!"
    else:
        return "You lose"

print(f"You chose: {player_choice}")
print(f"Computer chose: {computer_choice}")
print(determine_winner(player_choice,computer_choice))
