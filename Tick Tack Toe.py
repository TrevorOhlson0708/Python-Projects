def print_board(board):
    """
    Print the current state of the 3x3 board.
    board is a list of 9 elements: 'X', 'O', or ' '.
    """
    print()
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print()


def check_winner(board):
    """
    Return 'X' if X wins, 'O' if O wins, or None if no winner yet.
    """
    winning_lines = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),  
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8), 
        (2, 4, 6)
    ]

    for a, b, c in winning_lines:
        if board[a] == board[b] == board[c] and board[a] != ' ':
            return board[a]  # 'X' or 'O'

    return None


def is_board_full(board):
    """Return True if there are no empty spaces left."""
    return all(cell != ' ' for cell in board)


def get_player_move(board, player):
    """
    Ask the current player to choose a position (1-9).
    Keep asking until they pick a valid, empty spot.
    """
    while True:
        try:
            choice = int(input(f"Player {player}, choose a position (1-9): "))
        except ValueError:
            print("Please enter a number from 1 to 9.")
            continue

        if choice < 1 or choice > 9:
            print("That position is out of range. Choose 1-9.")
            continue

        index = choice - 1
        if board[index] != ' ':
            print("That spot is already taken. Choose another.")
            continue

        return index


def play_game():
    """
    Main game loop for a single Tic-Tac-Toe match.
    """
    board = [' '] * 9
    current_player = 'X'

    print("Welcome to Tic-Tac-Toe!")
    print("Positions are numbered like this:")
    print()
    print(" 1 | 2 | 3 ")
    print("---+---+---")
    print(" 4 | 5 | 6 ")
    print("---+---+---")
    print(" 7 | 8 | 9 ")
    print()

    while True:
        print_board(board)

        move_index = get_player_move(board, current_player)
        board[move_index] = current_player

        winner = check_winner(board)
        if winner:
            print_board(board)
            print(f"Player {winner} wins! 🎉")
            break

        if is_board_full(board):
            print_board(board)
            print("It's a draw! 🤝")
            break

        current_player = 'O' if current_player == 'X' else 'X'


def main():
    """
    Runs the game and asks if players want to play again.
    """
    while True:
        play_game()
        again = input("Play again? (y/n): ").strip().lower()
        if again != 'y':
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()
