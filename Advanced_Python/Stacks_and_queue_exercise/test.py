def create_board(size):
    board = []
    for i in range(size):
        board.append([None for x in range(size)])
    return board


def print_board(board):
    index = 0
    for line in board:
        print(f"{index}{line}")
        index += 1
    print("   0    1     2")


def player_turn(turns):
    if turns % 2 == 1:
        player = "O"
    else:
        player = "X"
    return player


def valid_position(row, col, size):
    if row < size and col < size:
        return True
    else:
        return False


def search_winner(board, player):
    count = 0
    for line in board:
        if line.count(player) == 3:
            return True
    for col in range(len(board)):
        for row in range(len(board)):
            if board[row][col] == player:
                count += 1
        if count == 3:
            return True
        count = 0
    for i in range(len(board)):
        if board[i][i] == player:
            count += 1
        if count == 3:
            return True
    count = 0
    for row in range(len(board)):
        if board[row][len(board) - row - 1] == player:
            count += 1
        if count == 3:
            return True
    count = 0
    return False


def full_board(board):
    for line in board:
        if None in line:
            return False
    return True


def play(board):
    print_board(board)
    turns = 0
    while True:
        player = player_turn(turns)
        if player == "X":
            print("Player_1 is your turn")
        else:
            print("Player_2 is your turn")
        player_row = int(input("Enter yuor row choice: "))
        player_column = int(input("Enter your column choise: "))
        print()
        print()
        if valid_position(player_row, player_column, size):
            if board[player_row][player_column] == None:
                board[player_row][player_column] = player
                turns += 1
                print_board(board)
            else:
                print("The position is busy")
                print("Please try another position")
                continue
        else:
            print("Invalid position")
            continue
        if search_winner(board, player):
            print(f"player {player} :: win the game!!")
            break
        if full_board(board):
            print("No more position on board")
            print("There is no winner!!!")
            break


size = 3
print("Welcome in sea chess")
board = create_board(size)
play(board)