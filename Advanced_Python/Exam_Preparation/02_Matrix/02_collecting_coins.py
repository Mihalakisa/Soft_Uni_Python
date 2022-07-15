from math import floor


def next_move(command, row, col, size):
    if command == 'up':
        if row - 1 < 0:
            return size - 1, col
        else:
            return row - 1, col
    if command == 'left':
        if col - 1 < 0:
            return row, size - 1
        else:
            return row, col - 1
    if command == 'right':
        if col + 1 >= size:
            return row, 0
        else:
            return row, col + 1
    if command == 'down':
        if row + 1 >= size:
            return 0, col
        else:
            return row + 1, col


size = int(input())
matrix = []
player_row, player_col = 0, 0
coins_result = 0
collected_coord = []
win_condition = False
lose_condition = False

for row in range(size):
    row_elements = input().split()
    for col in range(size):
        if row_elements[col] == 'P':
            player_row = row
            player_col = col
    matrix.append(row_elements)
collected_coord.append([player_row, player_col])


while True:
    if coins_result >= 100:
        win_condition = True
        break

    command = input()
    matrix[player_row][player_col] = '0'
    player_row, player_col = next_move(command, player_row, player_col, size)
    collected_coord.append([player_row, player_col])

    if matrix[player_row][player_col] == 'X':
        lose_condition = True
        coins_result /= 2
        break

    for row_index in range(size):
        for col_index in range(size):
            if (row_index, col_index) == (player_row, player_col):
                if matrix[row_index][col_index].isdigit():
                    coins_result += int(matrix[row_index][col_index])


if win_condition:
    print(f"You won! You've collected {coins_result} coins.")
    print("Your path:")
    for row in collected_coord:
        print(row)

elif lose_condition:
    print(f"Game over! You've collected {floor(coins_result)} coins.")
    print("Your path:")
    for row in collected_coord:
        print(row)
