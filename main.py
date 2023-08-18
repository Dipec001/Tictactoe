import random


def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)


def check_winner(board, player):
    # Check rows, columns, and diagonals for a win
    for i in range(3):
        if all([board[i][j] == player for j in range(3)]) or \
                all([board[j][i] == player for j in range(3)]):
            return True
    if all([board[i][i] == player for i in range(3)]) or \
            all([board[i][2 - i] == player for i in range(3)]):
        return True
    return False


def is_board_full(board):
    return all([cell != " " for row in board for cell in row])


def get_valid_input(prompt, low, high):
    while True:
        try:
            value = int(input(prompt))
            if low <= value <= high:
                return value
            else:
                print("Input out of range. Please enter a valid value.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def tic_tac_toe():
    player1 = input("Enter your name: ")

    while True:
        opponent_choice = input("Do you want to play against a friend or the computer? (friend/computer): ").lower()

        if opponent_choice == "friend":
            player2 = input("Enter your friend's name: ")
            break
        elif opponent_choice == "computer":
            player2 = "Computer"
            break
        else:
            print("Invalid response. Please choose 'friend' or 'computer'.")

    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    while True:
        print_board(board)

        if current_player == "X":
            row = get_valid_input(f"{player1}, enter row (0-2): ", 0, 2)
            col = get_valid_input(f"{player1}, enter column (0-2): ", 0, 2)
        else:
            if player2 == "Computer":
                row = random.randint(0, 2)
                col = random.randint(0, 2)
                print(f"{player2} selected row {row} and column {col}.")
            else:
                row = get_valid_input(f"{player2}, enter row (0-2): ", 0, 2)
                col = get_valid_input(f"{player2}, enter column (0-2): ", 0, 2)

        if board[row][col] == " ":
            board[row][col] = current_player
        else:
            print("Cell already occupied. Try again.")
            continue

        if check_winner(board, current_player):
            print_board(board)
            print(f"{player1 if current_player == 'X' else player2} wins!")
            break
        elif is_board_full(board):
            print_board(board)
            print("It's a draw!")
            break

        current_player = "O" if current_player == "X" else "X"


tic_tac_toe()
