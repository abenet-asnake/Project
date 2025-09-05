# Tic Tac Toe with Replay Option

def print_board(board):
    """Prints the game board with grid lines."""
    print("\n")
    for row in board:
        print(" | ".join(row))
        print("-" * 5)
    print("\n")

def check_winner(board, player):
    """Check all win conditions (rows, cols, diagonals)."""
    win_cond = [
        [board[0][0], board[0][1], board[0][2]],
        [board[1][0], board[1][1], board[1][2]],
        [board[2][0], board[2][1], board[2][2]],
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        [board[0][0], board[1][1], board[2][2]],
        [board[0][2], board[1][1], board[2][0]],
    ]
    return [player, player, player] in win_cond

def play_game():
    # Board setup with numbers for positions
    board = [["1", "2", "3"],
             ["4", "5", "6"],
             ["7", "8", "9"]]

    # Player symbol selection
    player1 = input("Player 1, choose X or O: ").upper()
    while player1 not in ["X", "O"]:
        player1 = input("Invalid choice! Choose X or O: ").upper()

    player2 = "O" if player1 == "X" else "X"
    print(f"✅ Player 1 is {player1}, Player 2 is {player2}\n")

    print("Game board positions:")
    print_board(board)

    players = [player1, player2]
    turn = 0

    for move in range(9):  # maximum 9 moves
        player = players[turn % 2]
        print(f"Player {player}'s turn")

        # Take input as position number (1–9)
        try:
            pos = int(input("Enter position (1-9): "))
        except ValueError:
            print("❌ Invalid input. Enter a number 1-9.")
            continue

        if pos < 1 or pos > 9:
            print("❌ Position out of range. Try again.")
            continue

        # Map position to row, col
        row, col = divmod(pos - 1, 3)

        # Check if cell is already taken
        if board[row][col] in ["X", "O"]:
            print("❌ Cell already taken, try again.")
            continue

        # Place player's move
        board[row][col] = player
        print(f"➡️ Player {player} placed at position {pos}")
        print_board(board)

        # Check for win
        if check_winner(board, player):
            print(f"🎉 Player {player} wins!")
            return  # end this round

        turn += 1
    else:
        print("🤝 It's a draw!")


def tic_tac_toe():
    """Main loop to allow replaying."""
    while True:
        play_game()
        again = input("Do you want to play another game? (yes/no): ").lower()
        if again not in ["yes", "y"]:
            print("👋 Thanks for playing! Goodbye!")
            break


# Run the game
tic_tac_toe()
