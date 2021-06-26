# Game intro
print("Rock...")
print("Paper...")
print("Scissors...")


# Game input
player_1 = input("Player 1, make your move: ")
player_2 = input("Player 2, make your move: ")

# Game Logic
if player_1 == "rock" and player_2 == "scissors":
    print("player 1 wins!")
elif player_1 == "rock" and player_2 == "paper":
    print("player 2 wins!")
elif player_1 == "paper" and player_2 == "rock":
    print("player 1 wins!")
elif player_1 == "paper" and player_2 == "scissors":
    print("player 2 wins!")
elif player_1 == "scissors" and player_2 == "paper":
    print("player 1 wins!")
elif player_1 == "scissors" and player_2 == "rock":
    print("player 1 wins!")
elif player_1 == player_2:
    print("It's a draw!")
else:
    print("Somehting went wrong")