"""
The minimax algorithm is a popular algorithm used in game theory and decision-making problems with two players.
It is particularly useful for games with perfect information, such as Tic-Tac-Toe, where both players have complete
knowledge of the game state. Determines the optimal decision in an adversarial game when you and your opponent have
opposite goals.

The goal of the minimax algorithm in this context is to determine the optimal move for the computer player by
searching through all possible moves and evaluating the resulting game states. It assumes that both players
will play optimally to maximize their chances of winning.

The minimax algorithm works by recursively evaluating the game states and assigning scores to them. It
alternates between maximizing the score for the computer player and minimizing the score for the human player,
assuming they will play optimally. The algorithm explores the game tree until it reaches a terminal state
(win, loss, or tie) and assigns a score to that state. It then backtracks and propagates the scores up the
tree, ultimately returning the best move for the current player.

In the context of Tic-Tac-Toe, the minimax algorithm allows the computer player to make optimal moves by
considering all possible moves and their resulting game states. It ensures that the computer will never
lose if a winning move is available, and it will force a tie if the human player plays optimally.

By using the minimax algorithm, the computer player in the code is made unbeatable, as it will always
choose the best move that leads to the highest chance of winning or forcing a tie.
"""

# The game constants define the size of the game board (3x3 for Tic-Tac-Toe),
# the symbol for empty cells (" "), the symbols for the player and the computer ("X" and "O")
BOARD_SIZE = 3
EMPTY_CELL = " "
PLAYER_SYMBOL = "X"
COMPUTER_SYMBOL = "O"

# Global variables for the scoreboard
scoreboard = {"wins": 0, "ties": 0, "losses": 0}


# Function to initialize the game state by creating an empty 3x3 board
def initialize_game():
    # Create an empty game board by filling it with empty cells
    board = [[EMPTY_CELL] * BOARD_SIZE for _ in range(BOARD_SIZE)]
    return board


# Function to display the current game board in the console window
def display_board(board):
    print("\nCurrent Board:")
    for row in range(BOARD_SIZE):
        # Print each row of the board with vertical separators
        print(" | ".join(board[row]))
        if row != BOARD_SIZE - 1:
            # Print horizontal separators between rows
            print("-" * (BOARD_SIZE * 4))


# This function prompts the player for their next move, checks if it's valid,
# and returns it as a tuple of (row, column).
def get_player_move(board):
    while True:
        try:
            # Get the player's move as an integer input
            move = int(input(f"\nEnter your move (1-{BOARD_SIZE ** 2}): "))
            if move < 1 or move > BOARD_SIZE ** 2:
                # Validate the move is within the valid range
                print(f"Invalid move. Please enter a number between 1 and {BOARD_SIZE ** 2}.")
            else:
                # Calculate the corresponding row and column based on the move
                # The calculation of row and col is achieved by subtracting 1 from move. This adjustment
                # makes the move variable zero-based, aligning it with array indexing conventions.
                # And then using the integer division // operator to determine the row and the modulo %
                # operator to determine the column. The result is intuitive as it corresponds
                # directly to the mathematical relationship between the move number and the grid
                # coordinates.
                row = (move - 1) // BOARD_SIZE
                col = (move - 1) % BOARD_SIZE
                if board[row][col] != EMPTY_CELL:
                    # Check if the chosen cell is already occupied
                    print("That cell is already occupied. Please choose an empty cell.")
                else:
                    return row, col
        except ValueError:
            # Handle invalid input that cannot be converted to an integer
            print(f"Invalid move. Please enter a number between 1 and {BOARD_SIZE ** 2}.")


# Function to generate the computer's next move
def get_computer_move(board):
    # This function uses the minimax algorithm to determine the computer's next move
    # by maximizing its own score and minimizing the player's score
    # We are only interested in the best_move value and not the best_score.
    # The _ is used as a placeholder to receive the best_score value, which we discard since we don't need it
    _, move = minimax(board, True)
    return move


# Function to check if the game is over, which occurs if there's a winner or if the board is full
def check_game_over(board):
    return check_winner(board) or check_board_full(board)


# This function checks if there's a winner by examining the rows, columns, and diagonals for three of the same symbols
def check_winner(board):
    # Check rows using generator expression
    for row in range(BOARD_SIZE):
        if all(cell == PLAYER_SYMBOL for cell in board[row]):
            return PLAYER_SYMBOL
        if all(cell == COMPUTER_SYMBOL for cell in board[row]):
            return COMPUTER_SYMBOL

    # Check columns using generator expression
    for col in range(BOARD_SIZE):
        if all(board[row][col] == PLAYER_SYMBOL for row in range(BOARD_SIZE)):
            return PLAYER_SYMBOL
        if all(board[row][col] == COMPUTER_SYMBOL for row in range(BOARD_SIZE)):
            return COMPUTER_SYMBOL

    # Check diagonals using generator expression
    # Check diagonal from top left to bottom right
    if all(board[i][i] == PLAYER_SYMBOL for i in range(BOARD_SIZE)):
        return PLAYER_SYMBOL
    if all(board[i][i] == COMPUTER_SYMBOL for i in range(BOARD_SIZE)):
        return COMPUTER_SYMBOL
    # Check diagonal from top right to bottom left
    if all(board[i][BOARD_SIZE - 1 - i] == PLAYER_SYMBOL for i in range(BOARD_SIZE)):
        return PLAYER_SYMBOL
    if all(board[i][BOARD_SIZE - 1 - i] == COMPUTER_SYMBOL for i in range(BOARD_SIZE)):
        return COMPUTER_SYMBOL

    return None


# This function checks if the board is full by scanning for any empty cells.
def check_board_full(board):
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            if board[row][col] == EMPTY_CELL:
                return False
    return True


# This function evaluates the score of the current board state: -1 if the player wins,
# 1 if the computer wins, or 0 if it's a tie
def evaluate(board):
    winner = check_winner(board)
    if winner == PLAYER_SYMBOL:
        return -1
    elif winner == COMPUTER_SYMBOL:
        return 1
    else:
        return 0


# This function uses the minimax algorithm to find the optimal move for the current player by exploring
# all possible moves
def minimax(board, is_maximizing):
    if check_game_over(board):
        return evaluate(board), None

    # First evaluated score will always be better than the current best_score for the maximizing player, and worse for
    # the minimizing player
    best_score = float("-inf") if is_maximizing else float("inf")
    best_move = None

    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            if board[row][col] == EMPTY_CELL:
                # Make a move on an empty cell
                board[row][col] = COMPUTER_SYMBOL if is_maximizing else PLAYER_SYMBOL
                # Recursively evaluate the resulting game state
                score, _ = minimax(board, not is_maximizing)
                # Undo the move
                board[row][col] = EMPTY_CELL

                if (is_maximizing and score > best_score) or (not is_maximizing and score < best_score):
                    best_score = score
                    best_move = (row, col)

    return best_score, best_move


# Function to update the scoreboard
def update_scoreboard(result):
    global scoreboard
    scoreboard[result] += 1


# Function to display the scoreboard
def display_scoreboard():
    global scoreboard
    print("\nScoreboard:")
    print("Wins:", scoreboard["wins"])
    print("Ties:", scoreboard["ties"])
    print("Losses:", scoreboard["losses"])


# Function to prompt the player to play again
def play_again():
    display_scoreboard()
    choice = input("Would you like to play again? (y/n): ")
    if choice.lower() == "y":
        play_game()
    else:
        print("Thank you for playing Tic-Tac-Toe!")


# Function to run the game
def play_game():
    global scoreboard
    print("Welcome to Tic-Tac-Toe!")
    print("You are playing as", PLAYER_SYMBOL)
    print("Make your move by entering the number corresponding to the cell.")
    print(f"The board is numbered from 1 to {BOARD_SIZE ** 2}, from top-left to bottom-right.")

    board = initialize_game()
    display_board(board)

    while True:
        if check_game_over(board):
            break

        # Player's move
        print("\nYour turn:")
        row, col = get_player_move(board)
        board[row][col] = PLAYER_SYMBOL
        display_board(board)

        if check_game_over(board):
            break

        # Computer's move
        print("\nComputer's turn:")
        row, col = get_computer_move(board)
        board[row][col] = COMPUTER_SYMBOL
        display_board(board)

    winner = check_winner(board)
    if winner == PLAYER_SYMBOL:
        print("\nYou win!")
        update_scoreboard("wins")
    elif winner == COMPUTER_SYMBOL:
        print("\nComputer wins!")
        update_scoreboard("losses")
    else:
        print("\nThe game is a tie!")
        update_scoreboard("ties")

    play_again()


# This conditional checks if the script is being run directly (as opposed to being imported as a module),
# and if so, it starts the game
if __name__ == "__main__":
    play_game()
