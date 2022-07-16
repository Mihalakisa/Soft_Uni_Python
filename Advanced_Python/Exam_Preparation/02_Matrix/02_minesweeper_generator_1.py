import re


def is_inside(row, col, size):
    return 0 <= row < size and 0 <= col < size


def count_neighbour_bombs(matrix, row, col):
    count = 0
    for r_move in range(-1, 2):
        for c_move in range(-1, 2):
            r_check = row + r_move
            c_check = col + c_move
            if is_inside(r_check, c_check, size) and matrix[r_check][c_check] == '*':
                count += 1

    return count


size = int(input())
matrix = []

for _ in range(size):
    matrix.append([None] * size)

bombs = int(input())
bomb_row, bomb_col = 0, 0

for _ in range(bombs):
    row, col = [int(x) for x in re.findall('\\d+', input())]
    matrix[row][col] = '*'

for row in range(size):
    for col in range(size):
        if matrix[row][col] == '*':
            continue
        cell_value = count_neighbour_bombs(matrix, row, col)
        matrix[row][col] = cell_value

for row in matrix:
    print(*row, sep=' ')
