import re


def is_inside(size, row, col):
    return 0 <= row < size and 0 <= col < size


def count_neighbour_bombs(matrix, row, col):
    count = 0
    if is_inside(len(matrix), row - 1, col) and matrix[row - 1][col] == '*':
        count += 1
    if is_inside(len(matrix), row + 1, col) and matrix[row + 1][col] == '*':
        count += 1
    if is_inside(len(matrix), row, col - 1) and matrix[row][col - 1] == '*':
        count += 1
    if is_inside(len(matrix), row, col + 1) and matrix[row][col + 1] == '*':
        count += 1
    if is_inside(len(matrix), row - 1, col - 1) and matrix[row - 1][col - 1] == '*':
        count += 1
    if is_inside(len(matrix), row + 1, col - 1) and matrix[row + 1][col - 1] == '*':
        count += 1
    if is_inside(len(matrix), row - 1, col + 1) and matrix[row - 1][col + 1] == '*':
        count += 1
    if is_inside(len(matrix), row + 1, col + 1) and matrix[row + 1][col + 1] == '*':
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
