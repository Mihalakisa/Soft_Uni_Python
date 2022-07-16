def is_inside(row, col, size):
    return 0 <= row < size and 0 <= col < size


player_one_name, player_two_name = input().split(', ')
player_one = 501
player_two = 501

size = 7
matrix = []
count = 0
result = 0
bulls_eye = False
p1_throw, p2_throw = 0, 0

for _ in range(size):
    matrix.append(input().split())

while player_one > 0 and player_two > 0:
    if bulls_eye:
        break
    count += 1
    data = input().replace('(', '').replace(')', '').split(', ')
    player_row, player_col = int(data[0]), int(data[1])

    if is_inside(player_row, player_col, size):
        for row_index in range(size):
            for col_index in range(size):
                if player_one <= 0 or player_two <= 0:
                    break
                if (row_index, col_index) == (player_row, player_col):
                    if matrix[row_index][col_index].isdigit():
                        if count % 2 == 0:
                            player_two -= int(matrix[row_index][col_index])
                            p2_throw += 1
                        else:
                            player_one -= int(matrix[row_index][col_index])
                            p1_throw += 1

                    elif matrix[player_row][player_col] == 'D':
                        result = (int(matrix[0][player_col]) + int(matrix[6][player_col])
                                + int(matrix[player_row][0]) + int(matrix[player_row][6])) * 2
                        if count % 2 == 0:
                            player_two -= result
                            p2_throw += 1
                        else:
                            player_one -= result
                            p1_throw += 1

                    elif matrix[row_index][col_index] == 'T':
                        result = (int(matrix[0][player_col]) + int(matrix[6][player_col])
                                + int(matrix[player_row][0]) + int(matrix[player_row][6])) * 3
                        if count % 2 == 0:
                            player_two -= result
                            p2_throw += 1
                        else:
                            player_one -= result
                            p1_throw += 1

                    elif matrix[row_index][col_index] == 'B':
                        bulls_eye = True
                        if count % 2 == 0:
                            p2_throw += 1
                            print(f"{player_two_name} won the game with {p2_throw} throws!")
                            break
                        else:
                            p1_throw += 1
                            print(f"{player_one_name} won the game with {p1_throw} throws!")
                            break
    else:
        if count % 2 == 0:
            p2_throw += 1
        else:
            p1_throw += 1


if player_one <= 0:
    print(f"{player_one_name} won the game with {p1_throw} throws!")
elif player_two <= 0:
    print(f"{player_two_name} won the game with {p2_throw} throws!")