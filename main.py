def print_board(board):
    for row in board:
        print(" | ".join(row))
        if row != board[-1]:
            print("-" * 9)


def check_win(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True

    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False


def is_full(board):
    return all(cell != " " for row in board for cell in row)


def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    print("Welcome to Tic Tac Toe!")

    while True:
        print_board(board)
        row, col = map(int, input(f"Player {current_player}, enter your row and column (e.g., 1 2): ").split())

        if row < 1 or row > 3 or col < 1 or col > 3 or board[row - 1][col - 1] != " ":
            print("Invalid move. Try again.")
            continue

        board[row - 1][col - 1] = current_player

        if check_win(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins! Congratulations!")
            break
        elif is_full(board):
            print_board(board)
            print("It's a draw!")
            break

        current_player = "O" if current_player == "X" else "X"


if __name__ == "__main__":
    main()
