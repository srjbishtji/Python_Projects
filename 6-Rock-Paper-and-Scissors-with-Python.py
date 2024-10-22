# In the rock, paper and scissors game our goal is to create a command-line game where a user has the option to choose between rock, paper and scissors and if the user wins the score is added, and at the end when the user finishes the game, the score is shown to the user.

# To create the Rock, Paper and Scissors game with Python, we need to take the user’s choice and then we need to compare it with the computer choice which is taken using the random module in Python from a list of choices, and if the user wins then the score will increase by 1.


# Code :

import random 
choices = ["Rock", "Paper", "Scissors"]
game = False
cpu_score = 0
player_score = 0
while not game:
    player = input("Rock, Paper and Scissors ? (Type 'End' to stop) ").capitalize()
    if player == "End":
        print("Final Scores:")
        print(f"CPU:{cpu_score}")
        print(f"Player:{player_score}")
        break
    if player not in choices:
        print("Invalid choice, please try again.")
        continue
    computer = random.choice(choices)
    if computer == player:
        print("Tie !!")
    elif player == "Rock":
        if computer == "Paper":
            print(f"You Lose !! {computer} covers {player}")
            cpu_score += 1
        else:
            print(f"You Win !! {player} smashes {computer}")
            player_score += 1
    elif player == "Paper":
        if computer == "Rock":
            print(f"You Win !! {player} covers {computer}")
            player_score += 1
        else:
            print(f"You Lose !! {computer} cut {player}")
            cpu_score += 1
    elif player == "Scissors":
        if computer == "Rock":
            print(f"You Lose !! {computer} smashes {player}")
            cpu_score += 1
        else:
            print(f"You Win !! {player} cut {computer}")
            player_score += 1