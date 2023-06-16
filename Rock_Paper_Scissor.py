
# Function to determine the winner between two moves
def determine_winner(player1_move, player2_move):
    if player1_move == player2_move:
        return "Draw"
    
    if (player1_move == 'R' and player2_move == 'S') or (player1_move == 'S' and player2_move == 'P') or (player1_move == 'P' and player2_move == 'R'):
        return "Player1"
    
    return "Player2"

# Play the game for 10 rounds
rounds = 10
player1_wins = 0
player2_wins = 0

for i in range(rounds):
    player1_move = input("Player 1, enter your move (R/P/S): ").upper()
    player2_move = input("Player 2, enter your move (R/P/S): ").upper()

    winner = determine_winner(player1_move, player2_move)

    if winner == "Player1":
        player1_wins += 1
    elif winner == "Player2":
        player2_wins += 1
    
    print("Game", i+1, ": Player 1 =", player1_move, ", Player 2 =", player2_move, ", Winner:", winner)
    print(" ")
# Determine the final winner
if player1_wins > player2_wins:
    print("Final Winner: Player1")
elif player1_wins < player2_wins:
    print("Final Winner: Player2")
else:
    print("Final Result: Draw")





