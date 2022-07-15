def get_next_pos(row, col, direction):
    if direction == 'up':
        return row - 1, col
    if direction == 'down':
        return row + 1, col
    if direction == 'left':
        return row, col - 1
    if direction == 'right':
        return row, col + 1


def is_outside(row, col, size):
    return row < 0 or col < 0 or row >= size or col >= size


text = input()
size = int(input())
matrix = []
player_row, player_col = 0, 0

for row in range(size):
    data = [x for x in input()]
    row_elements = data
    for col in range(size):
        if row_elements[col] == 'P':
            player_row = row
            player_col = col
    matrix.append(row_elements)

number_of_commands = int(input())

for _ in range(number_of_commands):
    command = input()
    current_row, current_col = get_next_pos(player_row, player_col, command)

    if is_outside(current_row, current_col, size):
        text = text[:len(text) - 1]
        matrix[player_row][player_col] = 'P'
        continue
    else:
        matrix[player_row][player_col] = '-'
        if matrix[current_row][current_col].isalpha():
            text += matrix[current_row][current_col]

    player_row, player_col = current_row, current_col
    matrix[current_row][current_col] = 'P'

print(text)
for row in matrix:
    print(''.join(row))
