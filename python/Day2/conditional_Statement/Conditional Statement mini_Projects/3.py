#7. Rock-Paper-Scissors game.
# 7. Rock-Paper-Scissors Game

player1 = input("Player 1 (Rock, Paper, Scissors): ")
player2 = input("Player 2 (Rock, Paper, Scissors): ")

if player1 == player2:
    print("It's a Tie!")

elif player1 == "Rock" and player2 == "Scissors":
    print("Player 1 Wins!")

elif player1 == "Paper" and player2 == "Rock":
    print("Player 1 Wins!")

elif player1 == "Scissors" and player2 == "Paper":
    print("Player 1 Wins!")

elif player2 == "Rock" and player1 == "Scissors":
    print("Player 2 Wins!")

elif player2 == "Paper" and player1 == "Rock":
    print("Player 2 Wins!")

elif player2 == "Scissors" and player1 == "Paper":
    print("Player 2 Wins!")

else:
    print("Invalid Input!")