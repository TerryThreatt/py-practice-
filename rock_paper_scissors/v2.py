# Game intro
print("Rock...")
print("Paper...")
print("Scissors...")


# Game input
player_1 = input("Player 1, make your move: ")
player_2 = input("Player 2, make your move: ")

# Game Logic - refactored logic from v1.py
if player_1 == player_2:
    print("It's a draw!")
elif player_1 == "rock":
    if player_2 == "scissors":
        print("player 1 wins!")
    if player_2 == "paper":
        print("player 2 wins!")
elif player_1 == "paper":
    if player_2 == "scissors":
        print("player 2 wins!")
    if player_2 == "rock":
        print("player 1 wins!")
elif player_1 == "scissors":
    if player_2 == "paper":
        print("player 1 wins!")
    if player_2 == "rock":
        print("player 2 wins!")
else:
    print("Somehting went wrong")