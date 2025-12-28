board = [" " for _ in range(9)]

def print_board():
    print()
    for i in range(0, 9, 3):
        print(board[i], "|", board[i+1], "|", board[i+2])
        if i < 6:
            print("--+---+--")
    print()

def check_winner(player):
    win_conditions = [
        [0,1,2], [3,4,5], [6,7,8],   # rows
        [0,3,6], [1,4,7], [2,5,8],   # columns
        [0,4,8], [2,4,6]             # diagonals
    ]
    return any(all(board[i] == player for i in combo) for combo in win_conditions)

current_player = "X"

for turn in range(9):
    print_board()
    move = int(input(f"Player {current_player}, choose position (1-9): ")) - 1

    if board[move] != " ":
        print("Spot already taken!")
        continue

    board[move] = current_player

    if check_winner(current_player):
        print_board()
        print(f"Player {current_player} wins!")
        break

    current_player = "O" if current_player == "X" else "X"
else:
    print_board()
    print("It's a draw!")
